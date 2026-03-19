from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
driver.maximize_window()
sleep(3)

driver.find_element(By.ID,"file-upload").send_keys(r"C:\Users\kiit2\Downloads\ResumeUpdated.pdf")
driver.find_element(By.ID,"file-submit").click()
sleep(2)

print(driver.find_element(By.ID,"uploaded-files").text)

sleep(30)
driver.quit()

