from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HtmlTestRunner


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()
        self.driver.get("https://shopifypages-shop1.myshopify.com/admin/auth/login")


    def test_login(self):
        driver = self.driver
        shopify_username = 'akorolchukwork@gmail.com'
        shopify_pass = 'qwertyui123'
        email_field_id = 'Login'
        pass_field_id = 'Password'
        login_button_id = "LoginSubmit"
        app_link_title = "Apps"
        #zp_app_title = "//A[@href='https://shopifypages-shop1.myshopify.com/admin/api_permissions/720994330/redirect'][text()='Zipify Pages (Staging)']"
        zp_app_title = "Zipify Pages (Staging)"
        pages_title = "Pages"

        email_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(email_field_id))
        pass_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(pass_field_id))
        login_button_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(login_button_id))

        email_field_element.clear()
        email_field_element.send_keys(shopify_username)
        pass_field_element.clear()
        pass_field_element.send_keys(shopify_pass)
        login_button_element.click()

        apps_link = WebDriverWait(driver, 50).until(lambda driver: driver.find_element_by_link_text(app_link_title))
        apps_link.click()

        zp_app_link = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text(zp_app_title))
        zp_app_link.click()

        #pages_app_title = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("//h1[text()='Pages']"))
        cr_page = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text("Create Page"))
        cr_page.click()




    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))