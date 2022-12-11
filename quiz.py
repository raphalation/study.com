from basepage import BasePage
from basepage import setup
from locations import *
import time


def quiz():
    driver = setup()
    base = BasePage(driver)
    base.open_url("https://study.com/member/my-dashboard.html#/studentAssignments")
    base.send_text("rr444@exeter.ac.uk", locations.username)
    base.send_text("n8wyVqeyyvMaLm5", locations.password)
    base.click(locations.login)
    base.find_element(locations.assignment_list)

    while base.exists(locations.assignment) is True:
        if base.exists(locations.show_lessons) is True:
            base.click(locations.show_lessons)
            base.click(locations.assignment_child)
        else:
            base.click(locations.assignment)
        base.click(locations.quiz)

        count = 0
        while base.exists(locations.retry) is False:
            count += 1
            correct = By.XPATH, f'(//label[@data-correct="true"]/input)[{count}]'
            next = By.XPATH, f'(//button[@ng-click="quizCtrl.submitAnswer()"])[{count}]'
            base.click(correct)
            base.click(next)
            time.sleep(1)

        base.open_url("https://study.com/member/my-dashboard.html#/studentAssignments")
        base.find_element(locations.assignment_list)


if __name__ == "__main__":
    quiz()
