# Generated by Django 4.0.5 on 2022-07-06 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao_cryptomoedas', '0003_moeda_valor_da_moeda_alter_moeda_moeda_a_acompanhar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moeda',
            name='VALOR_DA_MOEDA',
            field=models.CharField(choices=[('BTC', '20.278'), ('USD', '20.278'), ('BRL', '5.3866'), ('EUR', '1.0268'), ('ETH', '1.1454'), ('LTC', '228.533'), ('DOGE', '0.0674'), ('XRP', '0.32675')], default='BTC', max_length=100),
        ),
    ]
