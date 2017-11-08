from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HtmlTestRunner


class LoginTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")


    def test_login(self):
        driver = self.driver
        facebook_username = 'pittbulltest@yandex.ru'
        facebook_pass = 'pitttest'
        email_field_id = 'email'
        pass_field_id = 'pass'
        login_button_xpath = "//label[@id='loginbutton']"


        email_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(email_field_id))
        pass_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(pass_field_id))
        login_button_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login_button_xpath))

        email_field_element.clear()
        email_field_element.send_keys(facebook_username)
        pass_field_element.clear()
        pass_field_element.send_keys(facebook_pass)
        login_button_element.click()

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))