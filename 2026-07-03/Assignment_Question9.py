from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.amazon.com")
sleep(3)
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send_keys("Laptop", Keys.ENTER)
sleep(5)
titles = driver.find_elements(By.XPATH, "//h2//span")
for t in titles:
    print(t.text)
sleep(40)
driver.quit()