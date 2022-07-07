   
from django.db import models
import requests
class Moeda(models.Model):
   cotacoes= requests.get("https://economia.awesomeapi.com.br/json/last/BTC-USD,USD-BRL,BRL-USD,EUR-USD,LTC-USD,ETH-USD,DOGE-USD,XRP-USD")
   cotacoes = cotacoes.json()
   BITCOIN  =  'BTC'
   REAL_BRASILEIRO = 'BRL'
   EURO = "EUR"
   LITECOIN = "LTC"
   ETHEREUM = "ETH"
   DOGECOIN = "DOGE"
   XRP = "XRP"

   
   DATA_DA_MOEDA = [
      (BITCOIN, cotacoes['BTCUSD']["create_date"]),
      (REAL_BRASILEIRO, cotacoes['USDBRL']["create_date"]),
      (EURO , cotacoes['EURUSD']["create_date"]),
      (ETHEREUM, cotacoes['ETHUSD']["create_date"]),
      (LITECOIN, cotacoes['LTCUSD']["create_date"]),
      (DOGECOIN, cotacoes['DOGEUSD']["create_date"]),
      (XRP, cotacoes['XRPUSD']["create_date"]),
      ]
   
   DATA_DA_MOEDA = models.DateTimeField(
      max_length=100,
      choices=DATA_DA_MOEDA,
      default=BITCOIN,
      auto_now=False,
      auto_now_add=False,
      
       )      