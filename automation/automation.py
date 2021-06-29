from selenium import webdriver

chrome_path = r"C:\Users\Kamal Rathi\PycharmProjects\my_pythonProject\automation\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.get('http://www.google.com/')
