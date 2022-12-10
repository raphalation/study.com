from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



def setup():
    options = Options()
    options.add_argument("--disable-extensions")
    options.headless = False
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(executable_path=r"E:\REWARDS\1\BingRewards\drivers\chromedriver.exe", options=options)
    return driver
    
class BasePage(object):
    def __init__(self, driver, base_url='https://study.com/member/my-dashboard.html#/studentAssignments'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        
    def open_url(self, url):
        return self.driver.get(url)
    
    def find(self, locator):
        return self.driver.find_element(*locator)
        
    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return self.find(locator)
    
    def send_text(self, text, locator):
        return self.find_element(locator).send_keys(text)
        
    def click(self, locator):
        count = 0
        while count < 3:
            count += 1
            try:
                self.find_element(locator).click()
                return
            except ElementNotInteractableException:
                time.sleep(1)
        self.find_element(locator).click()

    def exists(self, locator):
        if len(self.driver.find_elements(*locator)) > 0:
            return True
        return False

    
