from selenium.webdriver.common.by import By


class locations(object):
    username = By.XPATH, '//input[@id="emailAddress"]'
    password = By.XPATH, '//input[@id="pwd"]'
    login = By.XPATH, '//button[@data-cname="login_page_login_button"]'
    assignment_list = By.XPATH, '//div[@class="assignments__list__header assignments__list__header--incomplete"]'
    incomplete_assignment = By.XPATH, '//div[@test-id="student_assignment_item_incomplete"]'
    assignment = By.XPATH, '(//div[@class="assignments__item__info"]/a)[1]'
    show_lessons = By.XPATH, '(//div[@class="assignments__item__info"])[1]/div[@ng-if="::assignment.childAssignments && assignment.childAssignments.length > 0"]/a'
    assignment_child = By.XPATH, '(//div[@class="assignments__item__info"]/a)[2]'
    quiz = By.XPATH, '//li[@class="quizTab "]'
    retry = By.XPATH, '//button[@class="btn btn-primary quiz__score__button"]'
