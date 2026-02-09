import requests
from tqdm import tqdm
import json

#yandex API
YANDEX_TOKEN = ''
YANDEX_BASE_URL = 'https://cloud-api.yandex.net'
YANDEX_FOLDER = 'PY-144'
yandex_headers = {
    'Authorization': f'OAuth {YANDEX_TOKEN}'
}
yandex_new_folder = f'{YANDEX_BASE_URL}/v1/disk/resources'
yandex_save_file = f'{YANDEX_BASE_URL}/v1/disk/resources/upload'

def yandex_create_folder(path):
    response = requests.put(
        yandex_new_folder,
        headers=yandex_headers,
        params={'path': path}
    )
    print("Создание папки Яндекс:", response.status_code)

    if response.status_code not in (201, 409):
        raise RuntimeError(f'Не удалось создать папку {path}')

def yandex_upload_file(url, disk_path, image_text):
    response = requests.post(
        yandex_save_file,
        params = {'path': disk_path, 'url' : url},
        headers=yandex_headers
    )
    #upload_link = response.json()['href']

    total_size = int(response.headers.get('content-length', 0))
    print("Размер передаваемого файла: ", total_size, " байт")
    file_info = dict(response.headers)
    print("Принятый заголовок ответа: ", file_info.items())

    with open(f"{image_text}.json", "w") as f:
        json.dump(file_info, f)

    print("Загрузка файла на Яндекс: ",response.status_code)
    print(response.json())
    if response.status_code == 202:
        print(f'Файл {disk_path} успешно загружен')
    else:
        print(f'Файл {disk_path} не загружен')

#
CATAAS_BASE_URL = 'https://cataas.com'

def cataas_create_image(image_text):
    cataas_path = f'{CATAAS_BASE_URL}/cat/says/{image_text}?json=true&width=100&height=100'
    response = requests.get(
        cataas_path
    )
    image_link = response.json()['url']
    print("create image: ", response.status_code)
    print(image_link)
    return image_link

def load_image_to_local_disk(image_link):
    cataas_path = f'{image_link}'
    response = requests.get(
        cataas_path,
        stream = True
    )
    total_size = int(response.headers.get('content-length', 0))

    progress_bar = tqdm(total=total_size, unit='B', unit_scale=True)

    print("Загрузка картинки: ", response.status_code, "Размер файла = ", total_size, " байт")


    # загрузка частями
    with open('image.jpg', 'wb') as f:
        for chunk in response.iter_content(chunk_size=100):
            f.write(chunk)
            progress_bar.update(len(chunk))
            #time.sleep(1)

    progress_bar.close()


def main():
    YANDEX_TOKEN = input('Введите свой токен: ')
    image_text = input('Привет! Введите волшебное слово для формирования картинки с котиком: ')
    image_link = cataas_create_image(image_text)

    #debug!
    load_image_to_local_disk(image_link)
    #stop

    disk_path = f'{YANDEX_FOLDER}/{image_text}.jpg'
    yandex_create_folder(YANDEX_FOLDER)
    yandex_upload_file(url=image_link, disk_path=disk_path, image_text=image_text)
    #stop

if __name__ == '__main__':
    main()
