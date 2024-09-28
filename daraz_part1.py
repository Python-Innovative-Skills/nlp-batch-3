from selenium import webdriver
from selenium.webdriver.common.by import By
import os
driver_path = os.path.join(os. getcwd(),'chromedriver-win64')
exe_path= os.path.join(driver_path,'chromedrivers.exe')

driver = webdriver.Chrome(exe_path)

driver.maximize_window()

driver.get('https://www.daraz.com.bd/products/-i168308069-s1962957262.html')

title= driver.find_element(By.XPATH,'//*[@id="module_product_title_1"]/div/div/h1').text

img = driver.find_element(By.XPATH,'//*[@id="module_item_gallery_1"]/div/div[1]/div/img').get_attribute('src')

print(title)
print(img)

print(title)
