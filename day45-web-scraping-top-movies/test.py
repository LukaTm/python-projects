from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

#yc_web_page = response.text
#soup = BeautifulSoup(yc_web_page, 'html.parser')

#hundred_movies = soup.find('div',attrs=)



#all_movies = soup.find_all(name='div',class_='jsx-3523802742')
#all_movies_new = all_movies.select('.jsx-3523802742 div ')
#all_movies_new = [element.select('div h3') for element in all_movies]

y = []
# for x in range(0,100):
#     all_movies = soup.find_all(f'[data-test="listicle-item-{x}"]')
#     #y.append(all_movies)
#     #movie_titles = [movie.getText() for movie in all_movies]
#     all_movies_new = [elem.select('h3') for elem in all_movies]
#
# all_movies = soup.find('h3',{'class': 'jsx-4245974604'})
# print(all_movies)

geckodriver_path = 'C:\Development\geckodriver.exe'
webdriver.Firefox.driver = geckodriver_path
driver = webdriver.Firefox()

driver.get('https://www.empireonline.com/movies/features/best-movies-2/')
driver.implicitly_wait(30)
html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
all_movies = soup.select('[data-test^="listicle-item-"] h3') # Nevajag ievadit item- kaut vai ir turpinajums
new_all_movies = [x.getText() for x in all_movies]
new_all_movies.reverse()


with open('movies100.txt',mode='w',encoding='utf-8') as file:
    for movie in new_all_movies:
        file.write(f'{movie}\n')




