import unittest
from appium import webdriver
import os
import resources as r
from time import sleep
from selenium.common import exceptions as excps
from testHelper import LoginHelper


class LoginTestSuite(unittest.TestCase):
    def setUp(self):
        self.directory = '%s/' % os.getcwd()
        self.file_name = "screenshot.png"

        self.caps = {'app': "d:\\omo\\app-debug_new.apk",
                     'platformName': 'Android',
                     'deviceName': "emulator-5554",
                     'appWaitActivity': ".MainActivity"
                     }

        self.login = LoginHelper(self.caps)

    def tearDown(self):
        self.login.__del__()

    def test_login_sucess(self):
        try:
            _phone_placeholder_text = self.login.get_phone_placeholder_text
            _password_placeholder_text = self.login.get_password_placeholder_text
            self.assertEqual(_phone_placeholder_text, r.phone_number_placeholder)
            self.assertEqual(_password_placeholder_text, r.password_placeholder)
            self.login.type_login(r.login_val)

            self.login.type_pwd(r.password_val)
            self.login.send_login_and_pwd()
            sleep(5)             # todo: should to be wait until, but there no IDs for elements, or Im too lazy

            self.login.take_screenshot(self.directory + self.file_name)

        except:     # yes, bare excepts is bad, but who didn't?
            self.fail("Failed, see logs")
            # todo: yes, should be logging here


if __name__ == '__main__':
    unittest.main()
