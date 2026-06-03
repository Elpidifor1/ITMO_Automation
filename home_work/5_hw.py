from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# поиск элемента
# 1 вариант - поиск всего блока
# icon = driver.find_element(By.CSS_SELECTOR, "#login_button_container")
# if icon is None:
#     print('Элементы не найдены')
# else:
#     print("Элементы найдены")

# 2 вариант - поиск элементов поштучно
def find_elements():

    username_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
    password_field = driver.find_element(By.CSS_SELECTOR, "#password")
    login_button  = driver.find_element(By.CSS_SELECTOR, "#login-button")

    if username_field and password_field and login_button:
        print('Элементы найдены')
    else:
        print("Элементы не найдены")

find_elements()