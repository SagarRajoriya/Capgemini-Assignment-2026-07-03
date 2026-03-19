from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demoqa.com/menu/")
driver.maximize_window()
sleep(3)

actions=ActionChains(driver)
main=driver.find_element(By.XPATH,"//a[text()='Main Item 2']")
actions.move_to_element(main).perform()
sleep(2)

sub = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='SUB SUB LIST »']")))
actions.move_to_element(sub).perform()

sleep(2)
driver.find_element(By.XPATH,"//a[text()='Sub Sub Item 1']").click()

sleep(30)
driver.quit()