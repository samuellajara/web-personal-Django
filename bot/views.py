from unittest import result
from django.shortcuts import render
from pprint import pprint
from sqlite3 import Timestamp
from binance.client import Client
from binance.enums import *
from binance.enums import HistoricalKlinesType
from binance.spot import Spot 
import datetime

# Create your views here.

API_KEY = ""
API_SECRET = ""

client = Client(API_KEY, API_SECRET, tld = 'com')
clients = Spot()


def bot(request):       
   lista_tickers = client.get_all_tickers()       
   return render(request, "bot/bot.html", {'datos': len(lista_tickers)})


def PRECIO_ACTUAL(request): 

   data_historical = clients.klines('BTCUSDT', Client.KLINE_INTERVAL_1MINUTE, limit = 1)

   if len(data_historical) == 1:
        precio_actual = data_historical[0][4]

   return render(request, "bot/PRECIO_ACTUAL.html", {'actual': precio_actual})



def MEDIA_MOVIL_4HS(request):

    data_historical = clients.klines('BTCUSDT', Client.KLINE_INTERVAL_4HOUR, limit = 200)

    if len(data_historical) == 200:
        sumatorio = 0
        for i in range((200 - 10), 200):
            sumatorio += float(data_historical[i][4]) #Sumamos los precios de cierre de todas las velas (4ºposicion de la lista)
        
        promedio = sumatorio / 10
        promedio = round(promedio, 3) #redondeo a un solos digito

      
    return render(request, "bot/MEDIA_MOVIL_4HS.html", {'ema4h': promedio})
  
              
   







   
"""
#from django.shortcuts import render

# Create your views here.

#def bot(request):

#   return render(request, "bot/bot.html")

"""
