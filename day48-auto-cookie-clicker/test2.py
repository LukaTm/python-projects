from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

geckodriver_path = 'C:\Development\geckodriver.exe'
webdriver.Firefox.driver = geckodriver_path
browser = webdriver.Firefox()
browser.get('http://github.com/')

#dates = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
#all_portals = driver.find_element(By.LINK_TEXT,'Farseer trilogy') # ! Pec teksa vnk mekle

#all_portals.click()

#search = driver.find_element(By.NAME,'search')
#search.send_keys('Mramkraskraksr') # send in input bar inputs
#search.submit() # uzpiez search button bet LKM var but gadijumi kad elementi nesakrit tur
#search.send_keys(Keys.ENTER) # IR vnk Enter Key so izmanto vnm sito labak vai kamer bus error submit()
#search.submit(Keys.F1) # !!!!!!!!!!!!! var jebkuru POGU IZVELETIES

signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

username_box = browser.find_element(By.ID, "login_field")
username_box.send_keys(USERNAME)
password_box = browser.find_element(By.ID, "password")
password_box.send_keys(PASSWORD)
password_box.submit()
time.sleep(3)
profile_link = browser.find_element(By.CLASS_NAME, "user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "LukaTm" in link_label # gives back AssertionError if false TAS IR NO MOSH
