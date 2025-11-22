import allure
from selene import browser


def test_open_browser_iphone():

    with allure.step("Открытие Яндекс в браузере Safari на iPhone"):
        browser.open("https://www.yandex.ru")
