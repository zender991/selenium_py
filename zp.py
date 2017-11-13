from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import unittest

import HtmlTestRunner


class LoginTest(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()


    def test_login(self):
        driver = self.driver
        self.driver.get("https://zp.mocstage.com/?shop=shopifypages-shop1.myshopify.com")

        driver.maximize_window()
        shopify_username = 'akorolchukwork@gmail.com'
        shopify_pass = 'qwertyui123'
        email_field_id = 'Login'
        pass_field_id = 'Password'
        login_button_id = "LoginSubmit"

        email_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(email_field_id))
        pass_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(pass_field_id))
        login_button_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(login_button_id))


        email_field_element.clear()
        email_field_element.send_keys(shopify_username)
        pass_field_element.clear()
        pass_field_element.send_keys(shopify_pass)
        login_button_element.click()

        cr_page = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_css_selector("a[title='Create Page']"))
        cr_page.click()

        create_template_button = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("(//button[text()='Use Template'])[2]"))
        create_template_button.click()

        page_title_field = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("page_create_title"))
        page_title_field.send_keys("qqqqwwwww")

        create_page_button = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("//button[text()='Create']"))
        create_page_button.click()

        script_label = WebDriverWait(driver, 10). until(lambda driver: driver.find_element_by_id("add-scripts"))


    def test_publish_page(self):

        driver = self.driver
        self.driver.get("https://zp.mocstage.com/?shop=shopifypages-shop1.myshopify.com")

        driver.maximize_window()
        shopify_username = 'akorolchukwork@gmail.com'
        shopify_pass = 'qwertyui123'
        email_field_id = 'Login'
        pass_field_id = 'Password'
        login_button_id = "LoginSubmit"

        email_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(email_field_id))
        pass_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(pass_field_id))
        login_button_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(login_button_id))

        email_field_element.clear()
        email_field_element.send_keys(shopify_username)
        pass_field_element.clear()
        pass_field_element.send_keys(shopify_pass)
        login_button_element.click()

        selected_page = WebDriverWait(driver, 30).until(lambda driver: driver.find_elements_by_css_selector("a[title='Constructor Page']"))
        selected_page[0].click()

        publish_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'publish-shared-popup')))
        publish_button.click()


    def test_update_page(self):

        driver = self.driver
        self.driver.get("https://zp.mocstage.com/?shop=shopifypages-shop1.myshopify.com")

        driver.maximize_window()
        shopify_username = 'akorolchukwork@gmail.com'
        shopify_pass = 'qwertyui123'
        email_field_id = 'Login'
        pass_field_id = 'Password'
        login_button_id = "LoginSubmit"

        email_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(email_field_id))
        pass_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(pass_field_id))
        login_button_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(login_button_id))

        email_field_element.clear()
        email_field_element.send_keys(shopify_username)
        pass_field_element.clear()
        pass_field_element.send_keys(shopify_pass)
        login_button_element.click()


        selected_page = WebDriverWait(driver, 30).until(lambda driver: driver.find_elements_by_css_selector("a[title='Constructor Page']"))
        selected_page[0].click()

        publish_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'publish-shared-popup')))
        publish_button.click()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))

