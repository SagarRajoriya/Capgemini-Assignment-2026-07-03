from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep


download_path=r"C:\Users\kiit2\Downloads"
options=webdriver.ChromeOptions()
prefs={"download.default_directory":download_path}
options.add_experimental_option("prefs",prefs)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/download")

sleep(3)

file=driver.find_element(By.XPATH,"(//div[@class='example']//a)[1]")
name=file.text
file.click()
sleep(5)

print("Downloaded" if name in os.listdir(download_path) else "Not Downloaded")

sleep(30)
driver.quit()