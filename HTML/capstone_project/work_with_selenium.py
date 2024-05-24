import selenium
from selenium.webdriver.common.by import By


class WWS:
    def __init__(self):
        self.get_start()

    def get_start(self):
        op = selenium.webdriver.ChromeOptions()
        op.add_experimental_option('detach', True)
        self.brows = selenium.webdriver.Chrome(options=op)
        self.brows.get(
            'https://docs.google.com/forms/d/e/1FAIpQLSdzGXNYrWWifhxSaHjcY15Aanuk0_ZLEFwZU8jI2_O4w5y2_A/viewform?usp=sf_link')

    def work(self, price, address, link):
        inp_price = self.brows.find_element(By.XPATH,
                                            value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        inp_price.click()
        inp_price.send_keys(price)
        inp_address = self.brows.find_element(By.XPATH,
                                              value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        inp_address.click()
        inp_address.send_keys(address)
        inp_link = self.brows.find_element(By.XPATH,
                                           value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        inp_link.click()
        inp_link.send_keys(link)

        buttom = self.brows.find_element(By.XPATH,
                                         value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")
        buttom.click()

        recall = self.brows.find_element(By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        recall.click()
