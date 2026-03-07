from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
sleep(3)
driver.switch_to.frame("iframeResult")
driver.switch_to.frame(0)
heading = driver.find_element(By.TAG_NAME, "h1").text
print("Heading:", heading)
sleep(40)
driver.quit()