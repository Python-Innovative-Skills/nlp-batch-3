from selenium import webdriver
from selenium.webdriver.common.by import By
import os
driver_path = os.path.join(os. getcwd(),'chromedriver-win64')
exe_path= os.path.join(driver_path,'chromedriver.exe')

driver = webdriver.Chrome(exe_path)

driver.maximize_window()

driver.get('https://www.daraz.com.bd/men-muslimin-shirts')

link_list =[]
for i in range(1,41):
    j=str(i)

    link= driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').get_attribute('href')

    link_list.append(link)

print(link_list)

# img = driver.find_element(By.XPATH,'//*[@id="module_item_gallery_1"]/div/div[1]/div/img').get_attribute('src')

# print(title)
# print(img)

# print(title)
