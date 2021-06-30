from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_path = r"C:\Users\Kamal Rathi\PycharmProjects\my_pythonProject\automation\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.maximize_window()

sleep(2)
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)
username = driver.find_element_by_name('username')
username.send_keys('username')
password = driver.find_element_by_name('password')
password.send_keys('password')
submit = driver.find_element_by_tag_name('form')
submit.submit()
sleep(4)
# notify_btn = driver.find_element_by_class_name('aOOlW')
# notify_btn.click()
# sleep(2)
messenger_btn = driver.find_element_by_class_name('Fifk5')
messenger_btn.click()
