# Navigate to Amazon and print all category names
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.amazon.in/")
sleep(4)
a = driver.find_elements("class name", "nav-sprite")
for item in a:
    print(item.text)

sleep(40)
driver.quit()
















