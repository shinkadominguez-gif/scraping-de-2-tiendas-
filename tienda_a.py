from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

def scrape_tienda_a():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []

    productos = soup.find_all('article', class_= 'product_pod')
    
    for producto in productos:
        titulo = producto.h3.a['title']

        precio = producto.find('p',class_='price_color').text.strip().encode('latin-1').decode('utf-8')
        precio = precio.replace('£', '')

        link = url + producto.h3.a['href']

        fecha = datetime.now().strftime('%Y-%m-%d')

        data.append({
            'tienda' : 'booksToScrape',
            'nombre' : titulo,
            'precio' : precio,
            'link' : link,
            'fecha' : fecha
        })

    return pd.DataFrame(data)
    