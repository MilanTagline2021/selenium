import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains 

def DeliveryOption(driver, send_to_someone):
    if not send_to_someone:
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/div/div/div[2]/div/div[6]/div/button[2]').click()
        time.sleep(4)
        driver.find_element_by_name('name').send_keys('Milan Sonani')
        time.sleep(4)
        driver.find_element_by_name('email').send_keys('milans.tagline@gmail.com')
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[1]/div/div/div/div[1]/div[3]/div/div/div/input').send_keys('+917600837364')
        time.sleep(5)
    else:
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[1]/input').send_keys('Ravi')
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div[2]/input').send_keys('Milan')
        time.sleep(4)
        driver.find_element_by_name('email').send_keys('ravik.tagline@gmail.com')
        time.sleep(4)
        send_to_someone=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[1]/div/div/div/div[1]/div[3]/div/label')
        driver.execute_script("arguments[0].click();",send_to_someone)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[1]/div/div/div/div[1]/div[4]/div[2]/div/div/ul/li[5]').click()
        time.sleep(5)

class Giftcardsby(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/mac/Downloads/chromedriver')

    # def test_in_sign_up_in_giftcards_by(self):
    #     driver = self.driver
    #     driver.get('https://myglobal.app/')
        
    #     driver.find_element_by_xpath("//*[@id='root']/div/div[2]/header/nav/div/div[2]/button").click()
    #     driver.find_element_by_name('companyName').send_keys("Tagline")
    #     driver.find_element_by_name('email').send_keys("hemal@yopmail.com")
    #     driver.find_element_by_name('password').send_keys("Tagline@123")
    #     driver.find_element_by_name('confirmPassword').send_keys("Tagline@123")
    #     driver.find_element_by_name('siteName').send_keys("hemal")
    #     driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div/p/span/input").click()
    #     driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div/button").click()

    #     assert "Sign up is not possible" not in driver.page_source

    # def test_contact_us(self):
        # driver = self.driver
        # driver.get('https://myglobal.app/contact')

        # driver.find_element_by_name('name').send_keys('hemal')
        # time.sleep(2)
        # driver.find_element_by_name('role').send_keys("devloper")
        # time.sleep(2)
        # driver.find_element_by_name('email').send_keys('hemal.tagline@gmail.com')
        # time.sleep(2)
        # driver.find_element_by_name('message').send_keys('this is testing.')
        # time.sleep(2)
        # submit = driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-default", " " ))]')
        # driver.execute_script("arguments[0].click();", submit)
        # time.sleep(2)

    # def test_on_publish_data(self):
        # driver = self.driver
        # driver.get('https://hemal.myglobal.app/login')

        # try:
        #     element = WebDriverWait(driver, 10).until(
        #         EC.presence_of_element_located((By.NAME, "password"))
        #     )
        #     element.send_keys('Tagline@123')
        #     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/form/div[5]/button').click()
            # dashboard = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div/div/div[1]/button"))
            # )
            # dashboard.click()
            # time.sleep(5)
            # dashboard.back()
            # time.sleep(5)
            # driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div/div[2]/div/button[1]").click() #click on publish button
            # time.sleep(5)
            # driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div[1]/p[1]/a").click() #click on privacy policy link
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="richtexteditor_1674121545_0_rte-edit-view"]/p').send_keys('a') #set value to privacy policy
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/button[2]').click() #click on save button to publish
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/nav/div[1]/a').click()
            # time.sleep(5)
            # driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div/div[2]/div/button[1]").click() #click on publish button
            # time.sleep(5)
            # driver.find_element_by_xpath("/html/body/div[7]/div/div/div[2]/div/div[1]/p[2]/a").click() #click on t&c link
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="richtexteditor_1872661978_0_rte-edit-view"]/p').send_keys('s') #set value in t&c
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/button[2]').click() #save button
            # time.sleep(5)


            # """Automation testing of Contact Support
            # """
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/nav/div[1]/a').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/button[1]').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div[1]/p[3]/a').click() #contact setting link
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div/form/div[2]/div/button').click() #click on edit button
            # time.sleep(5)
            # driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div/div/form/div[1]/div/div/div[1]/input").send_keys('9898989898')
            # time.sleep(5)
            # driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div/div/form/div[3]/div/div/input").send_keys('milans.tagline@gmail.com')
            # time.sleep(5)
            # driver.find_element_by_name('location').send_keys('surat')
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div/form/div[5]/div/button[1]').click()
            # time.sleep(5)

            # """Automation testing of base currency
            # """
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/nav/div[1]/a').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/button[1]').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div[1]/p[4]/a').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="left-tabs-example-tabpane-currency"]/div/div[2]/div/div[2]/div/ul/li[4]').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="left-tabs-example-tabpane-currency"]/div/div[2]/div/div[2]/div/button').click()
            # time.sleep(5)


            # """Automation testing of payment gateway
            # """
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/nav/div[1]/a').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/button[1]').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div[1]/p[5]/a').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="formGridCountry"]/option[2]').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/button[2]').click()
            # time.sleep(5)       
            # production = Select(driver.find_element_by_name('production'))
            # production.select_by_visible_text('Merit payment gateway')
            # driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div/button[2]').click()
            # time.sleep(5)
            

            # """Automation testing of subscription
            # """
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/nav/div[1]/a').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[2]/div/button[1]').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div/div[1]/p[6]/span').click()
            # time.sleep(5)
            # driver.find_element_by_xpath('//*[@id="pricing"]/div/div[2]/div/div/a').click()
            # time.sleep(20)
            # driver.find_elements_by_xpath('//*[@id="cb-body"]/div/div[2]/div[2]/button').click()
            # time.sleep(5)
            # driver.find_elements_by_xpath('//*[@id="cb-body"]/div/div[2]/div/button').click()
            # time.sleep(10)
            # driver.find_element_by_xpath('//*[@id="cb-body"]/div/div[2]/div/button/span').click()
            # time.sleep(5)            

        # except:
        #     "You are not able to logged in"


    # def test_for_admin_page(self):
    #     driver = self.driver
    #     driver.get('https://hemal.myglobal.app/login')
        
    #     element = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.NAME, "password"))
    #         )
    #     element.send_keys('Tagline@123')
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/form/div[5]/button').click()
    #     time.sleep(5)
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div[1]/div/button').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[2]/div/div[1]/div[1]/div/select/option[3]').click()
        # time.sleep(4)
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[2]/div/div[1]/div[2]/button').click()
        # time.sleep(4)
        # driver.find_element_by_xpath('//*[@id="inlineFormInputGroup_amount"]').send_keys('120')
        # time.sleep(4)
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div[2]/span/button').click()
        # time.sleep(5)
        # driver.refresh()
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div[1]').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div[2]/ul/li[6]').click()
        # time.sleep(5)
        # send_to_someone=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/div/div/div[2]/div/div[6]/div/button[1]')  
        
        # DeliveryOption(driver, send_to_someone)


    # def test_into_env(self):
    #     driver = self.driver
    #     driver.get('https://hemal.myglobal.app/login')
    #     driver.maximize_window()
        
    #     element = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.NAME, "password"))
    #         )
    #     element.send_keys('Tagline@123')
    #     time.sleep(3)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/form/div[5]/button').click()
    #     time.sleep(10)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/button').click()
    #     time.sleep(10)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/header/nav/div[2]/div/div[3]/div[1]/div/select/option[2]').click()
    #     time.sleep(7)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div[3]/div/div/div').click()
    #     time.sleep(4)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/div/div/div[2]/div/div[4]/div/div/div[2]/div/div[2]/ul/li[4]').click()
    #     time.sleep(4)
    #     send_to_someone=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[5]/div/div/div[2]/div/div[5]/div/button[1]')

    #     DeliveryOption(driver, send_to_someone)

    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[7]/div[2]/div/div/button').click()
    #     time.sleep(4)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[5]/div/div[4]/div[1]/div/select/option[3]').click()
    #     time.sleep(4)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[5]/div/div[4]/div[5]/button[2]').click()
    #     time.sleep(4)
    #     driver.find_element_by_name('name').send_keys('Milan')
    #     time.sleep(4)
    #     """Access using ActionChain
    #     """
    #     driver.find_element_by_id('cardNumber').click()
    #     ActionChains(driver).send_keys(4242424242424242).perform()
    #     time.sleep(4)
    #     driver.find_element_by_id('expiryDate').click()
    #     ActionChains(driver).send_keys(1025).perform()
    #     time.sleep(4)
    #     driver.find_element_by_id('cvv').click()
    #     ActionChains(driver).send_keys(100).perform()
    #     time.sleep(4)
    #     driver.find_element_by_xpath('//*[@id="root"]/div/div[5]/div/button').click()
    #     time.sleep(10)
    #     """Payment gateway javascript dynamically append so not get this dynamic values
    #     """
    #     # driver.find_element_by_class_name("form-field").send_keys('Checkout1!')
    #     driver.find_element_by_css_selector("input.form-field").send_keys('Checkout1!')#('//*[@id="password"]')
    #     # input_elmnt = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.form-field')))
    #     # action = ActionChains(driver)
    #     # action.move_to_element(input_elmnt).send_keys('Checkout1!').perform()

    #     time.sleep(3)
    #     submit = driver.find_element_by_xpath("//*[@id='txtButton']")
    #     driver.execute_script("arguments[0].click();", submit)
    #     # driver.find_element_by_xpath('//*[@id="txtButton"]').click()
    #     time.sleep(10)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
