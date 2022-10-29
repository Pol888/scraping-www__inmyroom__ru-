import datetime

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='D:\\programming\\Case888\\Python\\pars_pro\www__inmyroom__ru\\chromedriver.exe')
driver.get('https://esia.gosuslugi.ru/login/')

driver.maximize_window() # размер окна
#driver.minimize_window()

#user_name = driver.find_element_by_id("vb_login_username") # старый вариант ввода
#user_name = driver.find_element(By.ID, "navbar_username") //////  user_name = driver.find_element(By.XPATH, '//*[@id="navbar_password_hint"]')
#user_name.send_keys('pollove') # вводим name
#time.sleep(4)

user_name = driver.find_element(By.XPATH, '//*[@id="login"]')
user_name.send_keys('dpa777@inbox.ru')

user_password = driver.find_element(By.XPATH, '//*[@id="password"]')
user_password.send_keys('${CawBBQm4uc4r*')
time.sleep(10)
button_log = driver.find_element(By.XPATH, '//button[@class="plain-button plain-button_wide"]')
button_log.click()
time.sleep(5)

user_name = driver.find_element(By.XPATH, '//input[@id="login"]')
user_name.send_keys('dpa777@inbox.ru')

user_password = driver.find_element(By.XPATH, '//*[@id="password"]')
user_password.send_keys('${CawBBQm4uc4r*')
time.sleep(10)
button_log = driver.find_element(By.XPATH, '//button[@class="plain-button plain-button_wide"]')
button_log.click()
time.sleep(3)



#от левого верхнего угла отчет в пикселях (вправо, вниз)
#driver.execute_script('window.scrollTo(0, 500)')     # Пзволяет перемещаться по странице бегунком влево, вправо, вниз, вверх.


#action = ActionChains(driver)             #наведение на конкретный элемент
#r = driver.find_element(By.XPATH, '//div[@class="col span_9 push_1"]')
#action.move_to_element(r).perform()

time.sleep(5)

now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')  # скриншот
screenshot = 'scr' + now_date + '.png'
driver.save_screenshot(screenshot)

driver.refresh() # обнавление страници

driver.close()