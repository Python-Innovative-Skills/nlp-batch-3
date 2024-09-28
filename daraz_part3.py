from selenium import webdriver
from selenium.webdriver.common.by import By
import os
driver_path = os.path.join(os. getcwd(),'chromedriver-win64')
exe_path= os.path.join(driver_path,'chromedriver.exe')

driver = webdriver.Chrome(exe_path)

driver.maximize_window()

driver.get('https://www.daraz.com.bd/products/indispensable-quality-and-durablity-waterproof-motorcycle-raincoat-suit-for-men-innovative-qualityful-easy-to-care-and-longive-i320433736-s1482036254.html')
import time
time.sleep(50)

# scroll_height = driver.execute_script('return document.body.scrollHeight')
# import time
# for i in range(0,scroll_height,30):
#     driver.execute_script(f'window.scrollTo(0,{i});')
#     time.sleep(0.5)



# print(scroll_height)

# # img = driver.find_element(By.XPATH,'//*[@id="module_item_gallery_1"]/div/div[1]/div/img').get_attribute('src')

# # print(title)
# # print(img)

# # print(title)
