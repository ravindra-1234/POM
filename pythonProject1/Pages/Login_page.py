from selenium.webdriver.common.by import By
from time import *

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.XPATH,"//input[@name='username']")
        self.password_field = (By.XPATH,"//input[@name='password']")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.dashboard_element = (By.XPATH, "//h6[text()='Dashboard']")

    def open(self, url):
        self.driver.get(url)
        sleep(10)

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        sleep(20)

    def is_dashboard_displayed(self):
        return self.driver.find_element(*self.dashboard_element).is_displayed()
