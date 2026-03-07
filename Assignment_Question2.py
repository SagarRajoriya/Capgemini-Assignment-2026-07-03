#Print top 10 Movies from IMDB Top Chart
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
driver.get("https://www.imdb.com/chart/top/")
driver.maximize_window()
sleep(3)
movies = driver.find_elements(By.XPATH, "//h3[@class='ipc-title__text']")
for i in range(1,11):
    print(movies[i].text)

sleep(40)
driver.quit()