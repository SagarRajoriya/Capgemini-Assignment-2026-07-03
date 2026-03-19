
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://demoqa.com/select-menu")
sleep(3)
driver.find_element(By.ID, "withOptGroup").click()
sleep(2)
driver.find_element(By.XPATH, "//div[text()='Group 1, option 1']").click()
sleep(2)

sleep(40)
driver.quit()