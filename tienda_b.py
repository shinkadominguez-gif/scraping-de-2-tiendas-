from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from datetime import datetime

def scrape_tienda_b():
    data = []
    url = 'https://dataimport.com/'
    driver = webdriver.Chrome()
    driver.get(url)
    computadoras = driver.find_element(By.LINK_TEXT,'Computadoras')
    computadoras.click()
    monitores = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/ul/li[3]/a[2]')
    monitores.click()
    altura_actual = driver.execute_script('return document.body.scrollHeight')

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(4)

        nueva_altura = driver.execute_script('return document.body.scrollHeight')

        if altura_actual == nueva_altura:
            break
        altura_actual = nueva_altura

    productos = driver.find_elements(By.CLASS_NAME, 'product-col')

    for producto in productos:
        try:
            nombre = producto.find_element(By.CLASS_NAME, 'product-loop-title').text.strip()
        except:
            nombre = ''
        
        try:
            precio = producto.find_element(By.CLASS_NAME, 'price').text.strip()
        except:
            precio = ''

        try:
            garantia = producto.find_element(By.CLASS_NAME, 'stock').text.strip()
            garantia = garantia.replace('dÃas de garantia', 'dias')
        except:
            garantia = ''

        try:
            link_element = producto.find_element(By.CLASS_NAME, 'product-loop-title')
            link = link_element.get_attribute('href')
        except:
            link = ''

        try:
            fecha = datetime.now().strftime('%y-%m-%d')
        except:
            fecha = ''

        data.append({
            'tienda' : 'DataImport',
            'nombre' : nombre,
            'precio' : precio,
            'garantia' : garantia,
            'link' : link,
            'fecha' : fecha
        })
    return pd.DataFrame(data)

