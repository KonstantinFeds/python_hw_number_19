import os

import allure
from dotenv import load_dotenv

import config

load_dotenv()

USER_NAME_ANDROID = os.getenv("USER_NAME_ANDROID")
ACCESS_KEY_ANDROID = os.getenv("ACCESS_KEY_ANDROID")
URL = os.getenv("URL")

def attach_bstack_video_android(session_id):


    import requests
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(USER_NAME_ANDROID, ACCESS_KEY_ANDROID),
    ).json()
    #print(bstack_session)
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )