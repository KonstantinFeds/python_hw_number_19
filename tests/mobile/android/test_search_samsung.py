import allure
from selene import browser
from appium.webdriver.common.appiumby import AppiumBy


def test_search_samsung():

    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type(
        "Home"
    )
    browser.element((AppiumBy.XPATH, "//*[@text='Home Alone']")).click()
