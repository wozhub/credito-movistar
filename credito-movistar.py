#!/usr/bin/python

from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup

from credenciales import usuario, clave

display = Display(visible=0, size=(800, 600))
display.start()

print "Iniciando navegador..."
driver = webdriver.Firefox()
driver.get("https://online.movistar.com.ar/")

print "Iniciando sesion en movistar..."
elem = driver.find_element_by_id("userNamesmall")
elem.send_keys(usuario)
elem = driver.find_element_by_id("password-clear")
elem.send_keys(clave)
elem = driver.find_element_by_name("LoginForm")
elem.submit()

print "Obteniendo datos de la factura..."
elem = driver.find_element_by_id("miFactura")
soup = BeautifulSoup(elem.get_attribute("innerHTML"))
spans = soup.findAll('span')
factura = float(spans[1].text[1:].replace(',', '.'))

print "La factura va a ser por $ %s" % factura

print "Obteniendo datos sobre el saldo..."
driver.get("https://online.movistar.com.ar/altamira/consultaSaldo.do")

elem = driver.find_element_by_id("avisoSaldo")
soup = BeautifulSoup(elem.get_attribute("innerHTML"))
saldo = float(soup.find('strong').text[1:].replace(',', '.'))

print "Tengo $ %s de saldo" % saldo

driver.close()  # cierro el navegador
display.stop()  # termino el display virtual
