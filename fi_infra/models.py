from django.db import models

# Create your models here.
class Ativo(models.Model):
    ticker = models.CharField(max_length=10, primary_key=True)
    nome = models.CharField(max_length=255,default=None)
    taxa_adm = models.FloatField(default=None,null=True)
    juros = models.CharField(max_length=1, default=1,choices=(('1', 'mensal'),('6', 'semestral')))
    inicio = models.DateField(null=True)
    gestor = models.CharField(max_length=255,default=None,null=True)

class CotaPatrimonial(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticker = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    date =  models.DateTimeField(auto_now=True)
    cota_patrimonial = models.FloatField(default=None)
    patrimonio_liquido = models.FloatField(default=None)