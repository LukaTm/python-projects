from selenium import webdriver
from selenium.webdriver.common.by import By

geckodriver_path = 'C:\Development\geckodriver.exe'
webdriver.Firefox.driver = geckodriver_path
driver = webdriver.Firefox()
driver.get('https://www.python.org/')

dates = driver.find_elements(By.CSS_SELECTOR,'.event-widget time')
events = driver.find_elements(By.CSS_SELECTOR,'.event-widget li a')

# x = []
# for time in events:
#     x = time.text
#
# y = []
# for date in dates:
#     y.append(date.text) # cant do x = time.text jo vislaik replacos un paliks pedejais cipars



eventss = {}

for n in range(len(events)):
    eventss[n] = {
        dates[n].text:events[n].text
    }















