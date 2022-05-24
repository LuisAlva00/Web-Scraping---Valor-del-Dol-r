#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


url='https://www.cronista.com/MercadosOnline/dolar.html'
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
compra=soup.find_all('div',class_='buy-value')
venta=soup.find_all('div',class_='sell-value')
titulos=soup.find_all('td',class_='name')

dolar_compra=[i.text for i in compra]
dolar_compra.insert(2,'------')
dolar_compra

dolar_venta=[i.text for i in venta]
print(dolar_venta)

t=[i.text for i in titulos]
print(t)


# In[3]:


cotizaciones={'TIPOS DE DOLÃRES':t,'COMPRA':dolar_compra,'VENTA':dolar_venta}
print(cotizaciones)

df=pd.DataFrame(cotizaciones)
ordenando=df.sort_values('VENTA',ascending=True)
ordenando

plt.figure(figsize=(7,8))
plt.scatter(ordenando['TIPOS DE DOLÃRES'],ordenando['VENTA'])
plt.xticks(rotation='60')
plt.show()

