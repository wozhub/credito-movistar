#!/usr/bin/python

# Modo debug mediante environment variable
from os import getenv

from pyvirtualdisplay import Display
from selenium import webdriver

from credenciales import usuario, clave

visible = getenv('VISIBLE') or 0
display = Display(visible=visible, size=(800, 600))
display.start()


driver = webdriver.Firefox()
driver.get("https://online.movistar.com.ar/")

elem = driver.find_element_by_id("userNamesmall")
elem.send_keys(usuario)
elem = driver.find_element_by_id("password-clear")
elem.send_keys(clave)
elem = driver.find_element_by_name("LoginForm")
elem.submit()

driver.get("https://online.movistar.com.ar/autogestion/secured/owner/implLoadPrepaidOverview.do")
for e in driver.find_elements_by_tag_name("span"):
    if "$" in e.text:
        break

saldo = float(e.text[1:].replace(',', '.'))
print saldo

if getenv("EXTENDIDO"):
    for e in driver.find_elements_by_tag_name("table"):
        print e.text

driver.close()  # cierro el navegador
display.stop()  # termino el display virtual
