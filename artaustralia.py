# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

path = r'/Users/mac/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get("https://artguide.com.au/")

driver.find_elements(By.XPATH, '/html/body/nav[1]/div/div/ul[1]/li[1]/a')[0].click()
time.sleep(5)
driver.find_elements(By.XPATH, '/html/body/section[1]/div/div/nav/ul/li[1]/a')[0].click()
time.sleep(5)
driver.find_elements(By.XPATH, '/html/body/section[2]/div/article[1]/a')[0].click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, 'header__subscribe-btn')
time.sleep(10)
driver.back()
time.sleep(3)
driver.find_elements(By.XPATH, '/html/body/nav[1]/div/div/ul[1]/li[2]/a')[0].click()
print("move to studio blog")
time.sleep(2)
driver.find_elements(By.XPATH, '/html/body/section[1]/div/article/div/div[2]/a')[0].click()
time.sleep(2)
print("move on photo")
driver.find_elements(By.XPATH, '/html/body/section[1]/div/div/div/div/figure[1]/a')[0].click()
print("close photo")
time.sleep(2)
driver.find_elements(By.ID, 'swipebox-close')[0].click()


# elements=driver.find_elements_by_tag_name('a')
# # print(elements.text)
# for element in elements:
#     # print(element)
#     print(element.get_attribute('href'))


# try:
#     elements = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@href]"))
#     )
#     # for element in elements:
#     #     print(element.text)
#     print(elements)
# finally:
#     driver.quit()
# driver.quit()
