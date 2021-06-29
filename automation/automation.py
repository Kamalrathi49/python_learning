from selenium import webdriver

chrome_path = r"C:\Users\Kamal Rathi\PycharmProjects\my_pythonProject\automation\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.get('https://www.seleniumeasy.com/test/')

print("Selenium Easy - Best Demo website to practice Selenium Webdriver" in driver.title)
