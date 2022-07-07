
from django.db import models
import requests
import json


# Create your models here.
from django.db import models

# Classe da Moeda

class Moeda(models.Model):
      
   #Definição da Moeda pela qual fará a conversão da cotação   
   
   DOLAR_AMERICANO = 'USD'
   
   MOEDA_BASE = [
      
      (DOLAR_AMERICANO , 'Dolar Americano')
      
   ]
   MOEDA_BASE = models.CharField(
      max_length=20,
      choices=MOEDA_BASE,
      default=DOLAR_AMERICANO
      )
   
   # Definição das siglas para a base de daddos
   
   BITCOIN = 'BTC' 
   DOLAR_AMERICANO = 'USD'
   REAL_BRASILEIRO = 'BRL'
   EURO = "EUR"
   LITECOIN = "LTC"
   ETHEREUM = "ETH"
   DOGECOIN = "DOGE"
   XRP = "XRP"
   
   #Moeda pela qual será desejado o acompanhamento
   
   MOEDA_A_ACOMPANHAR = [
      (BITCOIN , 'BTC'),
      (REAL_BRASILEIRO , 'Real Brasileiro'),
      (EURO , 'Euro'),
      (LITECOIN , 'Litecoin'),
      (ETHEREUM , 'Ethereum'),
      (DOGECOIN , 'Dogecoin'),
      (XRP, 'XRP'),
      ]
  
   MOEDA_A_ACOMPANHAR = models.CharField(
      max_length=20,
      choices=MOEDA_A_ACOMPANHAR,
      default=BITCOIN
       )   
   
   #importação das moedas utilizadas pela Api: "awesomeapi"

   cotacoes= requests.get("https://economia.awesomeapi.com.br/json/last/BTC-USD,USD-BRL,BRL-USD,EUR-USD,LTC-USD,ETH-USD,DOGE-USD,XRP-USD")
   cotacoes = cotacoes.json()
   BITCOIN  =  'BTC'
   REAL_BRASILEIRO = 'BRL'
   EURO = "EUR"
   LITECOIN = "LTC"
   ETHEREUM = "ETH"
   DOGECOIN = "DOGE"
   XRP = "XRP"

   #escolha apenas do valor da moeda desejada dentro da tabela de moedas do "".awesomeapi"
   
   VALOR_DA_MOEDA = [
      (BITCOIN, cotacoes['BTCUSD']["bid"]),
      (REAL_BRASILEIRO, cotacoes['USDBRL']["bid"]),
      (EURO , cotacoes['EURUSD']["bid"]),
      (ETHEREUM, cotacoes['ETHUSD']["bid"]),
      (LITECOIN, cotacoes['LTCUSD']["bid"]),
      (DOGECOIN, cotacoes['DOGEUSD']["bid"]),
      (XRP, cotacoes['XRPUSD']["bid"]),
      ]
   
   VALOR_DA_MOEDA = models.CharField(
      max_length=100,
      choices=VALOR_DA_MOEDA,
      default=BITCOIN
      
       )   
 
   # Visualização na tabela   
   def __str__(self):
    return "%s (%s)" %(self.MOEDA_A_ACOMPANHAR, self.MOEDA_BASE,)
   def __str__(self):
      return self.VALOR_DA_MOEDA
  





    
    
    
    
    
    
    
    
    
    
    
 

