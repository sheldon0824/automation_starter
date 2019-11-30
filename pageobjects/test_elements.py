import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://k1-test.gengee.com/en/#/login")
driver.implicitly_wait(2)
driver.find_element_by_xpath("//*[@id='username']").send_keys("eutestqa2")
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin123")
driver.find_element_by_xpath("//*/input[@class='dropdown-value']").click()
# driver.find_element_by_xpath("//*/li[contains(text(),'Deutschland')]").click()
driver.find_element_by_xpath("//*/li[@class='dropdown-item'][2]").click()
driver.find_element_by_xpath("//*[@type='submit']").click()
time.sleep(2)
# textContent
# innerText
print(driver.find_element_by_xpath("//*/span[@class='username']").get_attribute(''))

driver.quit()

