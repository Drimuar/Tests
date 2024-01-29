import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


@pytest.fixture
def open_main_page():
    browser.get('https://learn.javascript.ru/')
    print("\n Открытие главной страницы")


def test_case1(open_main_page):
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
    email_input.send_keys("Varp12@mail.ru")
    name_input = browser.find_element(By.ID, 'register-displayName')
    name_input.clear()
    name_input.send_keys("Эдуард Б")
    pas_input = browser.find_element(By.ID, 'register-password')
    pas_input.clear()
    pas_input.send_keys("HP55ddACBBqYXT")
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
