
from locations import locations

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

    
def setup():
    options = Options()
    options.add_argument("--disable-extensions")
    options.headless = False
    driver = webdriver.Chrome(executable_path=r"E:\REWARDS\1\BingRewards\drivers\chromedriver.exe", options=options)
    return driver
    
driver = setup()
driver.get("https://study.com/member/my-dashboard.html#/studentAssignments")
driver.find_element(*locations.username).send_keys("123")