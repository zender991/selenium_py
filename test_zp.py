from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

import HtmlTestRunner



class LoginTest(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        #self.driver.get("https://shopifypages-shop1.myshopify.com/admin/auth/login")


    def test_login(self):
        driver = self.driver
        self.driver.get("https://shopifypages-shop1.myshopify.com/admin/auth/login")
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

        apps_link = WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_link_text(app_link_title))
        apps_link.click()

        #zp_app_link = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text(zp_app_title))
        #zp_app_link.click()

        elements1 = WebDriverWait(driver, 30).until(lambda driver: driver.find_elements_by_link_text("Zipify Pages (Staging)"))
        elements1[0].click()

        #windowhanles = driver.window_handles[1]
        #driver.SwitchTo().Window(driver.WindowHandles.Last())
        window_before = driver.window_handles[0]
        print(window_before)

        driver.switch_to.window(driver.window_handles[-1])

        window_after = driver.window_handles[0]

        print(window_after)



        #cr_page = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_link_text("V-Day 2: Order Bump"))
        #cr_page.click()
        #cr_page = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("//a[text()='Create Page']/@href"))

        #cr_page = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("(//a[@href='/pages/templates?shop=shopifypages-shop1.myshopify.com'])[1]"))
        #cr_page = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_xpath("(//a[contains(@title,'Create Page')])[2]"))
        cr_page = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_css_selector("a[title='Create Page']"))
        cr_page.click()

        #element = WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_css_selector("a[title='Create Page']"))
        #driver.execute_script("arguments[0].click();", element)
        #driver.execute_script("document.getElementsByClassName('zpa-button zpa-button-create xh-highlight')[0].click()")

        #driver.get("https://zp.mocstage.com/?shop=shopifypages-shop1.myshopify.com")

        #create_template_button = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("(//button[text()='Use Template'])[2]"))
        #create_template_button.click()

        elements = WebDriverWait(driver, 30).until(lambda driver: driver.find_elements_by_xpath("//button[text()='Use Template']"))
        elements[1].click()

        page_title_field = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id("page_create_title"))
        page_title_field.send_keys("qqqqwwwww")

        create_page_button = WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath("//button[text()='Create']"))
        create_page_button.click()

    def test_publish_page(self):
        driver = self.driver
        self.driver.get("https://zp.mocstage.com/pages/3840/constructor/?shop=shopifypages-shop1.myshopify.com")

        publish_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("publish-shared-popup"))
        publish_button.click()

    '''def test_update_page(self):
        driver = self.driver

        update_button = publish_button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("publish-shared-popup"))
        publish_button.click()'''



    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))