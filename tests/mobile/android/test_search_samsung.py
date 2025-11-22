import allure
from selene import browser
from appium.webdriver.common.appiumby import AppiumBy


def test_search_samsung():

    with allure.step("Клик для активации строки поиска"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    with allure.step("Ввод в строку поиска значения 'Home'"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
            "Home"
        )

    with allure.step("Клик по статье 'Home Alone'"):
        browser.element((AppiumBy.XPATH, "//*[@text='Home Alone']")).click()
