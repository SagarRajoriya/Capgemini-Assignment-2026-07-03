from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.google.com")
search = driver.find_element(By.NAME,"q")
search.send_keys("laptop")
sleep(3)
suggestions = driver.find_elements(By.XPATH,"//li[@role='presentation']")
for s in suggestions:
    print(s.text)
sleep(40)
driver.quit()