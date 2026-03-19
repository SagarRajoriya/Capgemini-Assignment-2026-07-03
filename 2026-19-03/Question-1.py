from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()

driver.maximize_window()

driver.get("https://demowebshop.tricentis.com")

sleep(2)

driver.find_element(By.LINK_TEXT, "Books").click()
driver.find_elements(By.CSS_SELECTOR, ".product-box-add-to-cart-button")[0].click()
sleep(2)

driver.find_element(By.LINK_TEXT, "Shopping cart").click()
sleep(2)
assert len(driver.find_elements(By.CSS_SELECTOR, ".cart-item-row")) > 0
print("Product present in cart")


driver.quit()