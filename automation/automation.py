from selenium import webdriver

chrome_path = r"C:\Users\Kamal Rathi\PycharmProjects\my_pythonProject\automation\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

user_msg = driver.find_element_by_id("user-message")
sm_button = driver.find_element_by_class_name('btn-default')
user_msg.clear()
user_msg.send_keys("hello")


sm_button.click()

output_message = driver.find_element_by_id("display")
print(output_message.get_attribute("innerHTML"))

assert 'hello' in output_message.text

driver.close()

