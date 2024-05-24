import time

import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
number = '574751211'
password = 'zk.,k.,juf'
chrome_op = selenium.webdriver.ChromeOptions()
chrome_op.add_experimental_option('detach', True)

driver = selenium.webdriver.Chrome(chrome_op)
driver.get(
    'https://tinder.com/app/recs')
registr = driver.find_element(By.LINK_TEXT, value='Войдите')
registr.click()
time.sleep(2)

enty_in_facebook = driver.find_element(By.XPATH,
                                       value="//*[@id='u647161393']/main/div/div/div[1]/div/div/div[2]/div["
                                             "2]/span/div[2]/button/div[2]/div[2]/div/div")
enty_in_facebook.click()
first_window = driver.window_handles[0]
second_window = driver.window_handles[1]
driver.switch_to.window(second_window)

acept_cookies = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]")
acept_cookies.click()
time.sleep(1)
write_num = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
write_num.click()
write_num.send_keys(number)
write_password = driver.find_element(By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
write_password.click()
write_password.send_keys(password, Keys.ENTER)
time.sleep(1)
# confirm = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div/div/div/div/div['
#                                               '1]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/div/div/div['
#                                               '1]/div/div/div/div/div')
# confirm.click()
driver.switch_to.window(first_window)
enter_num = driver.find_element(By.XPATH, value="/html/body/div[2]/main/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/input")
enter_num.click()
enter_num.send_keys(number, Keys.ENTER)
