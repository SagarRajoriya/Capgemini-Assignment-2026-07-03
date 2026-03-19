from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
sleep(3)

driver.find_element(By.LINK_TEXT,"Books").click()
sleep(2)

driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[2]").click()
sleep(2)

driver.find_element(By.LINK_TEXT,"Shopping cart").click()
sleep(2)

products=driver.find_elements(By.XPATH,"//td[@class='product']/a")
print("2 products added" if len(products)==2 else "Not correct")

sleep(30)
driver.quit()