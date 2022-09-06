from django.db import models
from django.db import IntegrityError

from fi_infra.models import CotaPatrimonial
from fi_infra.models import Ativo
from fi_infra.worker.assets import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import datetime
import schedule

# Setting up logger
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, handlers=[logging.FileHandler("fi_infra/worker/anbima_scraper.log"),logging.StreamHandler()])
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Selenium scrapper
def scrap_anbima(fundo,url):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)

    try:
        cota_patrimonial = float(WebDriverWait(driver, 20).until(presence_of_element_located((By.ID, "periodicosValorDaCota-0"))).text.replace('.','').replace(',','.'))
        patrimonio_liquido = float(WebDriverWait(driver, 20).until(presence_of_element_located((By.ID, "periodicosPatrimonioLiquido-0"))).text.replace('.','').replace(',','.'))
        inicio = WebDriverWait(driver, 20).until(presence_of_element_located((By.CSS_SELECTOR, '#output__container--primeiroAporte div > span'))).text 
        gestor = WebDriverWait(driver, 20).until(presence_of_element_located((By.CSS_SELECTOR, '#output__container--prestadoresGestores div > span'))).text 
        try:
            obj = Ativo.objects.get(ticker=fundo)
        except Ativo.DoesNotExist:
            obj = Ativo(ticker=fundo, nome=driver.title.split("|")[0], inicio=datetime.datetime.strptime(inicio, "%d/%m/%Y").strftime("%Y-%m-%d"), gestor=gestor)
            obj.save()
            logger.critical(fundo+": Adicionado novo fundo.")

        cotacao = CotaPatrimonial(ticker_id=fundo, cota_patrimonial=cota_patrimonial, patrimonio_liquido=patrimonio_liquido)
        cotacao.save()
        logger.info(fundo+" - cota_patrimonial: %s",cota_patrimonial)

    except NoSuchElementException as e: 
        logger.error("%s"+ str(e), " Anbima element not found. "+fundo, exc_info=1)
        pass
    
    except TimeoutException as e: 
        logger.error(fundo+" Anbima response error. ", exc_info=1)
        pass
    
    time.sleep(5)
    driver.quit()
    
def daily_scrap():
    logger.warning("10:20, buscando dados diarios no site da ANBIMA.")
    for i in range(len(ativos)):
        scrap_anbima(**ativos[i])

# Routines
schedule.every().day.at("10:20").do(daily_scrap)

# run daily_scrap now, when server restarts.
daily_scrap()

# check if there is pending schedule every 15 min.
while True:
    schedule.run_pending()
    time.sleep(900)
