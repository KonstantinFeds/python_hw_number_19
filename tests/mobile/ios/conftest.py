import os
import allure
import pytest
from dotenv import load_dotenv
from selenium.webdriver import Remote
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions
from tests.mobile.ios.utils.allure import attach_bstack_video_ios


load_dotenv()

USER_NAME_IOS = os.getenv("USER_NAME_IOS")
ACCESS_KEY_IOS = os.getenv("ACCESS_KEY_IOS")
URL = os.getenv("URL")


@pytest.fixture(scope="function", autouse=True)
def macos_management():

    with allure.step("Настройка конфигураций под IOS для BrowserStack "):

        options = ChromeOptions()

        capabilities = {
            "browserName": "Safari",
            "browserVersion": "latest",
            "platformName": "ios",
            "deviceName": "iPhone 14 Pro Max",
            "platformVersion": "16",
            "bstack:options": {
                "projectName": "IOS Safari tests",
                "buildName": "browserstack-build-safari",
                "userName": USER_NAME_IOS,
                "accessKey": ACCESS_KEY_IOS,
                "osVersion": "16",
                "deviceName": "iPhone 14 Pro Max",
                "realMobile": "true",
                "local": "false",
            },
        }

    # Добавляем capabilities в options
    for key, value in capabilities.items():
        options.set_capability(key, value)

    driver = Remote(command_executor=URL, options=options)

    browser.config.driver = driver
    browser.config.timeout = 10.0

    yield

    session_id = browser.driver.session_id

    with allure.step('Закрытие сессии'):
        browser.quit()

    attach_bstack_video_ios(session_id)
