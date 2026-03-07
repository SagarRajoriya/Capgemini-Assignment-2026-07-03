from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.amazon.com")
sleep(3)
account = driver.find_element(By.ID, "nav-link-accountList")
actions = ActionChains(driver)
actions.move_to_element(account).perform()
sleep(2)
driver.find_element(By.LINK_TEXT, "Create a List").click()

sleep(40)
driver.quit()
