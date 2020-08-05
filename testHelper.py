from appium import webdriver
from time import sleep
import resources as r

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginHelper:

    def __init__(self, caps):
        self.__driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        sleep(15)     # ¯\_(ツ)_/¯ see below
        # WebDriverWait(self.__driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        self.__phone_field = self.__driver.find_element_by_accessibility_id(r.phone_id)
        self.__password_field = self.__driver.find_element_by_accessibility_id(r.password_id)
        self.__sign_in_btn = self.__driver.find_element_by_accessibility_id(r.signup_btn_id)

    def type_login(self, _text):
        self.__phone_field.send_keys(_text)
        sleep(1)

    @property
    def get_phone_placeholder_text(self):
        return self.__phone_field.text

    def type_pwd(self, _text):
        self.__password_field.send_keys(_text)
        sleep(1)

    @property
    def get_password_placeholder_text(self):
        return self.__password_field.text

    def send_login_and_pwd(self):
        self.__sign_in_btn.click()
        sleep(10)
        self.__driver.find_element_by_accessibility_id(r.entrance_key_btn_id).is_displayed()

    def take_screenshot(self, dest):
        self.__driver.save_screenshot(dest)

    def __del__(self):
        self.__driver.quit()