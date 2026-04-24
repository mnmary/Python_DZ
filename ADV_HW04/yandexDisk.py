import requests
from dotenv import load_dotenv
import os

# load const from .env file
load_dotenv()

# create a Telegram bot
YANDEX_TOKEN = os.environ.get("TOKEN")

mkdir_url = 'https://cloud-api.yandex.net:443/v1/disk/resources'


def create_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': YANDEX_TOKEN}
    create_dir = requests.api.put(mkdir_url, headers=headers, params=params)
    return create_dir.status_code


def delete_folder(path: str):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': YANDEX_TOKEN}
    create_dir = requests.api.delete(mkdir_url, headers=headers, params=params)
    return create_dir.status_code

import unittest
class TestYandex(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_success_create_folder(self):
        self.assertEqual(create_folder('1111222333'), 201)

    def tearDown(self):
        # Удаляем папку после прохождения теста на создание папки
        delete_folder('test')
        print('method tearDown')


if __name__ == '__main__':
    unittest.main()