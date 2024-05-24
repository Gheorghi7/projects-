import datetime
import json

import time
import selenium
from selenium.webdriver.common.by import By


class TwitterBot:
    def __init__(self):
        self.down = None
        self.up = None
        self.internetSpeed()
        self.write_in_note()

    def internetSpeed(self):
        option_ch = selenium.webdriver.ChromeOptions()
        option_ch.add_experimental_option('detach', True)
        self.driver = selenium.webdriver.Chrome(options=option_ch)
        self.driver.get('https://www.speedtest.net/')

        buttom_accept = self.driver.find_element(By.XPATH,
                                                 value="/html/body/div[5]/div[2]/div/div/div[2]/div/div/button")
        buttom_accept.click()
        time.sleep(1)
        go = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go.click()
        time.sleep(50)
        close_congrat = self.driver.find_element(By.XPATH,
                                                 value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button")
        close_congrat.click()
        time.sleep(1)
        download = self.driver.find_element(By.XPATH,
                                            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.down = download.text
        upload = self.driver.find_element(By.XPATH,
                                          value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.up = upload.text

    def write_in_note(self):
        data = {
            'DataTime': datetime.datetime.now().strftime("%d,%m,%Y %H:%M:%S"),
            'Download': self.down,
            'Upload': self.up
        }
        try:
            with open('data.txt', 'a') as wr:
                wr.write(f"{data}\n")
        except FileNotFoundError:
            with open('data.txt', 'wr') as wr:
                wr.write(f"{data}\n")
