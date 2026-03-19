from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

options = ChromeOptions()
options.add_experimental_option("detach",True)

driver = Chrome(options = options)
driver.maximize_window()
driver.get("https://demoqa.com/select-menu")

driver.find_element(By.ID,"withOptGroup").click()
driver.find_element(By.XPATH,"//div[text()='Group 2, option 1']").click()
sleep(2)
value=driver.find_element(By.XPATH,"//div[@id='withOptGroup']//div[contains(@class,'singleValue')]").text

print(value)

sleep(30)
driver.quit()