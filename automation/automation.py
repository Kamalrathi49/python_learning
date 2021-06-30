from selenium import webdriver

chrome_path = r"C:\Users\Kamal Rathi\PycharmProjects\my_pythonProject\automation\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')


sm_button = driver.find_element_by_class_name('btn-default')

user_message = driver.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys("helllooooooo")

sm_button.click()

message = driver.find_element_by_id("display")
print(message.get_attribute("innerHTML"))

