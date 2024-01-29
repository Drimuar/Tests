import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

@pytest.fixture
def login():
    login = "Varp12@mail.ru"
    return login
@pytest.fixture
def name():
    name = "Эдуард Б."
    return name
@pytest.fixture
def password():
    password = "HP55ddACBBqYXT"
    return password
@pytest.fixture
def open_main_page():
    browser.get('https://learn.javascript.ru/')
    print("\n Открытие главной страницы")


def test_case1(open_main_page, login, password, name):
    print("\n Регистрация нового пользователя")
    open_main_page
    auth_button = browser.find_element(By.CLASS_NAME, 'sitetoolbar__login')
    auth_button.click()
    time.sleep(2)
    regform_button = browser.find_element(By.CLASS_NAME, 'login-form__button-link')
    regform_button.click()
    time.sleep(2)
    email_input = browser.find_element(By.ID, 'register-email')
    email_input.clear()
    email_input.send_keys(login)
    name_input = browser.find_element(By.ID, 'register-displayName')
    name_input.clear()
    name_input.send_keys(name)
    pas_input = browser.find_element(By.ID, 'register-password')
    pas_input.clear()
    pas_input.send_keys(password)
    time.sleep(1)
    agreement_checkbox = browser.find_element(By.ID, 'accept-agreement')
    agreement_checkbox.click()
    reg_button = browser.find_element(By.CLASS_NAME, 'submit')
    reg_button.click()
    time.sleep(5)
    success_text = browser.find_element(By.CSS_SELECTOR, "div.login-form__success > p")  
    print(success_text.text)
    print(success_text.text == "С адреса notify@javascript.ru отправлено письмо со ссылкой-подтверждением.")
    assert success_text.text == "С адреса notify@javascript.ru отправлено письмо со ссылкой-подтверждением."

def test_case2(open_main_page, login, password, name):
    print("\n Авторизация существующего пользователя")
    open_main_page
    auth_button = browser.find_element(By.CLASS_NAME, 'sitetoolbar__login')
    auth_button.click()
    time.sleep(2)
    email_input = browser.find_element(By.ID, 'auth-email')
    email_input.clear()
    email_input.send_keys(login)
    pas_input = browser.find_element(By.ID, 'auth-password')
    pas_input.clear()
    pas_input.send_keys(password)
    time.sleep(1)
    sub_button = browser.find_element(By.CSS_SELECTOR, 'div.login-form__submit > button')
    sub_button.click()
    time.sleep(5)
    success_text = browser.find_element(By.CSS_SELECTOR, "button.sitetoolbar__user > span")
    print(success_text.text)
    print(name)
    assert success_text.text == name
    
