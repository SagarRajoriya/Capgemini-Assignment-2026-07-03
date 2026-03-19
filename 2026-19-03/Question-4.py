from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.maximize_window()


driver.get("https://the-internet.herokuapp.com/dynamic_controls")
sleep(3)
driver.find_element(By.XPATH,"//button[text()='Remove']").click()


wait=WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Add']"))).click()


sleep(30)
driver.quit()