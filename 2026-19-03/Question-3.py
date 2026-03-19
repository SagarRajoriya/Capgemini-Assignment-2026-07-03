from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



o = ChromeOptions()
o.add_experimental_option("detach",True)

driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.find_element(By.XPATH,"//button").click()

text=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"finish")))
sleep(30)
driver.quit()

