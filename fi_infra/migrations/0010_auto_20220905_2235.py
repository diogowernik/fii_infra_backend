# Generated by Django 3.0.2 on 2022-09-06 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fi_infra', '0009_auto_20220905_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotapatrimonial',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fi_infra.Ativo'),
        ),
    ]
