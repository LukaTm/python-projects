import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:

    def __init__(self):
        self.geckodriver_path = 'C:\Development\geckodriver.exe'
        webdriver.Firefox.driver = self.geckodriver_path
        self.driver = webdriver.Firefox()

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(1)
        button = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        button.click()
        # click_go = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[1]')
        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        # click_go.click()
        time.sleep(40)
        down = self.driver.find_element(By.CLASS_NAME, 'download-speed')
        up = self.driver.find_element(By.CLASS_NAME, 'upload-speed')
        print(down.text)
        print(up.text)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/')
        log_in = self.driver.find_element(By.CLASS_NAME, 'css-4rbku5')
        log_in.click()
        email = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        email.send_keys('email')
        next = self.driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next.click()
        time.sleep(2)
        try:
            username = self.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys('@user')
            next2 = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
            next2.click()
        except:
            pass
        finally:
            time.sleep(1)
            password = self.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys('password')
            time.sleep(1)
            log_in2 = self.driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            log_in2.click()
            time.sleep(4)
            message = self.driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span')
            time.sleep(1)
            message.click()
            time.sleep(1)
            message2 = self.driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
            message2.send_keys('Why is it that ')
            time.sleep(1)
            tweet = self.driver.find_element(By.XPATH,
                                             '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
            time.sleep(1)
            tweet.click()


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()
