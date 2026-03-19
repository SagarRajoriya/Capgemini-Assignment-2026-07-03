from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
sleep(3)

driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
sleep(1)

driver.switch_to.alert.accept()
sleep(1)

print(driver.find_element(By.ID,"result").text)


sleep(30)
driver.quit()