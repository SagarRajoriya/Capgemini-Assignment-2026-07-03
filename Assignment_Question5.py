from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.amazon.in/")
sleep(3)
links = driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.text)
sleep(40)
driver.quit()