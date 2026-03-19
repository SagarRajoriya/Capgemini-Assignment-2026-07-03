from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com")
driver.maximize_window()
sleep(3)

driver.find_element(By.LINK_TEXT,"Books").click()
sleep(3)

books=driver.find_elements(By.XPATH,"//div[@class='product-item']")

for b in books:
    price=float(b.find_element(By.CLASS_NAME,"price").text.replace("$",""))
    if price<20:
        b.find_element(By.XPATH,".//input[@value='Add to cart']").click()
        sleep(1)

sleep(30)
driver.quit()