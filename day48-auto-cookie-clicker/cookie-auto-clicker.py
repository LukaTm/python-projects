import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

geckodriver_path = 'C:\Development\geckodriver.exe'
webdriver.Firefox.driver = geckodriver_path
browser = webdriver.Firefox()
browser.get('http://orteil.dashnet.org/experiments/cookie/')

timeout = time.time() + 60*5



cookie = browser.find_element(By.ID, 'cookie')
cursor = browser.find_element(By.CSS_SELECTOR, "#store #buyCursor")
grandma = browser.find_element(By.ID, 'buyGrandma')
Factory = browser.find_element(By.ID, 'buyFactory')
Mine = browser.find_element(By.ID, 'buyMine')
Shipment = browser.find_element(By.ID, 'buyShipment')
money = browser.find_element(By.ID, 'money')


fift = browser.find_element(By.CSS_SELECTOR, '#buyCursor b').text.split()[2].replace(',', '')
hunded = browser.find_element(By.CSS_SELECTOR, '#buyGrandma b').text.split()[2].replace(',', '')
fifthund = browser.find_element(By.CSS_SELECTOR, '#buyFactory b').text.split()[2].replace(',', '')
two_thousnd = browser.find_element(By.CSS_SELECTOR, '#buyMine b').text.split()[2].replace(',', '')
seven_thous = browser.find_element(By.CSS_SELECTOR, '#buyShipment b').text.split()[2].replace(',', '')

while True:
    cookie.click()
    try:
        money_integer = int(money.text)
        if money_integer > int(seven_thous):
            Shipment.click()
        elif money_integer > int(two_thousnd):
            Mine.click()
        elif money_integer > int(fifthund):
            Factory.click()
        elif money_integer > int(hunded):
            grandma.click()
        elif money_integer > int(fift):
            cursor.click()
    except selenium.common.exceptions.StaleElementReferenceException:
        cursor = browser.find_element(By.CSS_SELECTOR, "#store #buyCursor")
        grandma = browser.find_element(By.ID, 'buyGrandma')
        Factory = browser.find_element(By.ID, 'buyFactory')
        mine = browser.find_element(By.CSS_SELECTOR, "#store #buyMine")
        shipment = browser.find_element(By.CSS_SELECTOR, "#store #buyShipment")
        money = browser.find_element(By.ID, 'money')
    if time.time() > timeout:
        break






























