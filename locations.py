from selenium.webdriver.common.by import By

class locations(object):
    username = By.XPATH, '//input[@id="emailAddress"]'
    password = By.XPATH, '//input[@id="pwd"]'
    login = By.XPATH, '//button[@data-cname="login_page_login_button"]'
    assignment_list = By.XPATH, '//div[@class="assignments__list__header assignments__list__header--incomplete"]'
    assignment = By.XPATH, '(//div[@class="assignments__item__info"]/a)[1]'
    quiz = By.XPATH, '//li[@class="quizTab "]'
    retry = By.XPATH, '//button[@class="btn btn-primary quiz__score__button"]'