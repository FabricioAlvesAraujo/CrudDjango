# Generated by Django 4.0.5 on 2022-07-06 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao_cryptomoedas', '0007_alter_moeda_data_da_moeda_alter_moeda_valor_da_moeda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moeda',
            name='DATA_DA_MOEDA',
            field=models.CharField(blank=True, choices=[('2022-07-06 20:32:27', '2022-07-06 20:32:27'), ('2022-07-06 18:30:42', '2022-07-06 18:30:42'), ('2022-07-06 20:32:29', '2022-07-06 20:32:29'), ('2022-07-06 20:32:05', '2022-07-06 20:32:05'), ('2021-09-06 04:32:37', '2021-09-06 04:32:37'), ('2022-07-06 20:32:14', '2022-07-06 20:32:14'), ('2022-07-06 20:32:26', '2022-07-06 20:32:26')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='MOEDA_BASE',
            field=models.CharField(choices=[('USD', 'Dolar Americano')], default='USD', max_length=20),
        ),
        migrations.AlterField(
            model_name='moeda',
            name='VALOR_DA_MOEDA',
            field=models.CharField(choices=[('BTC', '20.574'), ('BRL', '5.4294'), ('EUR', '1.0182'), ('ETH', '1.19358'), ('LTC', '228.533'), ('DOGE', '0.06891'), ('XRP', '0.33356')], default='BTC', max_length=100),
        ),
    ]
