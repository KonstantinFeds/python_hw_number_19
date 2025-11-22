import os
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser
from tests.mobile.android.utils.allure import attach_bstack_video_android

load_dotenv()

USER_NAME_ANDROID = os.getenv("USER_NAME_ANDROID")
ACCESS_KEY_ANDROID = os.getenv("ACCESS_KEY_ANDROID")
URL = os.getenv("URL")


@pytest.fixture(scope="function", autouse=True)
def mobile_management():

    with allure.step("Настройка конфигураций под android для BrowserStack "):

        options = UiAutomator2Options().load_capabilities(
            {
                # Specify device and os_version for testing
                "platformName": "android",
                "platformVersion": "12.0",
                "deviceName": "Samsung Galaxy S21",
                # Set URL of the application under test
                "app": "bs://sample.app",
                # Set other BrowserStack capabilities
                "bstack:options": {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    # Set your access credentials
                    "userName": USER_NAME_ANDROID,
                    "accessKey": ACCESS_KEY_ANDROID,
                },
            }
        )

    browser.config.driver = webdriver.Remote(URL, options=options)

    yield

    session_id = browser.driver.session_id

    with allure.step("Закрытие сессии"):
        browser.quit()

    attach_bstack_video_android(session_id)
