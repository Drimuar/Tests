import pytest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

@pytest.fixture
def authorization(open_main_page, login, password):
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
    time.sleep(2)



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
    success_text = browser.find_element(By.CSS_SELECTOR, "div.login-form__success > p").text 
    print(success_text)
    print(success_text == "С адреса notify@javascript.ru отправлено письмо со ссылкой-подтверждением.")
    assert success_text == "С адреса notify@javascript.ru отправлено письмо со ссылкой-подтверждением."


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
    success_text = browser.find_element(By.CSS_SELECTOR, "button.sitetoolbar__user > span").text
    print(success_text.text)
    print(name)
    assert success_text == name


def test_case3(authorization):
    print("\n Обновление имени пользователя")
    authorization
    auth_button = browser.find_element(By.CLASS_NAME, 'sitetoolbar__user')
    auth_button.click()
    time.sleep(1)
    link = browser.find_element(By.LINK_TEXT, "Аккаунт")
    link.click()
    time.sleep(2)
    name_block = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/main/div/div/div/div[2]/section[1]/div/div[2]/ul/li[1]/form/div[1]")
    name_block.click()
    name_imput = browser.find_element(By.NAME, "displayName")
    name_imput.clear()
    name_imput.send_keys("Эдуард")
    name_imput.send_keys(Keys.ENTER)
    time.sleep(1)
    success_text = browser.find_element(By.CSS_SELECTOR, "div.notification_success > div.notification__content").text
    assert success_text == "Ваше имя пользователя изменено."
    
    
def test_case4(open_main_page):
    print("\n Авторизация существующего пользователя")
    open_main_page
    toFind = "замыкания"
    find_field = browser.find_element(By.CLASS_NAME, 'text-input__frontpage-search__input')
    find_field.click()
    find_field.send_keys(toFind)
    find_field.send_keys(Keys.ENTER)
    time.sleep(3)
    result = browser.find_element(By.CLASS_NAME, 'search-results__marked').text
    assert toFind.upper() in result.upper()