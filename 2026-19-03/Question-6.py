from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep

driver=webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()
sleep(3)

multi=driver.find_element(By.ID,"cars")
ActionChains(driver).move_to_element(multi).perform()

select=Select(multi)
select.select_by_visible_text("Volvo")
select.select_by_visible_text("Saab")
select.select_by_visible_text("Opel")

for option in select.all_selected_options:
    print(option.text)

sleep(30)
driver.quit()