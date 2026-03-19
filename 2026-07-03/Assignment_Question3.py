#Count the Number of Images
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.amazon.com")
sleep(5)
images = driver.find_elements(By.TAG_NAME, "img")
print("Total images:", len(images))
sleep(40)
driver.quit()