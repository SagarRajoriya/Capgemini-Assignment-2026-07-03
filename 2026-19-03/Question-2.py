from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

options = ChromeOptions()

options.add_experimental_option("detach",True)

driver = Chrome(options=options)

driver.maximize_window()

driver.get("https://demowebshop.tricentis.com")

sleep(1)

driver.find_element(By.LINK_TEXT, "Electronics").click()

sleep(1)

driver.find_element(By.XPATH,"//div[@class='sub-category-item']//a[contains(text(),'Cell phones')]").click()

sleep(30)
driver.quit()

