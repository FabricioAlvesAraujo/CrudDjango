# Generated by Django 4.0.5 on 2022-07-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao_cryptomoedas', '0004_alter_moeda_valor_da_moeda'),
    ]

    operations = [
        migrations.AddField(
            model_name='moeda',
            name='DATA_DA_MOEDA',
            field=models.DateTimeField(choices=[('BTC', '2022-07-06 18:53:56'), ('BRL', '2022-07-06 18:30:42'), ('EUR', '2022-07-06 18:53:40'), ('ETH', '2022-07-06 18:53:24'), ('LTC', '2021-09-06 04:32:37'), ('DOGE', '2022-07-06 18:53:33'), ('XRP', '2022-07-06 18:53:47')], default='BTC', max_length=100),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='MOEDA_A_ACOMPANHAR',
            field=models.CharField(choices=[('BTC', 'BTC'), ('BRL', 'Real Brasileiro'), ('EUR', 'Euro'), ('LTC', 'Litecoin'), ('ETH', 'Ethereum'), ('DOGE', 'Dogecoin'), ('XRP', 'XRP')], default='BTC', max_length=20),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='VALOR_DA_MOEDA',
            field=models.CharField(choices=[('BTC', '20.34'), ('BRL', '5.4294'), ('EUR', '1.0181'), ('ETH', '1.16149'), ('LTC', '228.533'), ('DOGE', '0.06832'), ('XRP', '0.3291')], default='BTC', max_length=100),
        ),
    ]
