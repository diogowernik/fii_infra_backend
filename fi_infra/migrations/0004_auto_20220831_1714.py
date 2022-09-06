# Generated by Django 3.0.2 on 2022-08-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fi_infra', '0003_ativo_ticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ativo',
            name='ticker',
            field=models.CharField(max_length=10),
        ),
    ]
