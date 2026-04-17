import requests
from bs4 import BeautifulSoup
from datetime import datetime

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'программисты', 'приглашение']

def logger(path):
    def __logger(old_function):
        def create_log_string(*args, **kwargs):
            dt = datetime.now()
            func = old_function.__name__
            result = old_function(*args, **kwargs)

            log = f'Дата и время: {dt}\n'+f'Функция: {func}\n'+f'Результат: {result}\n'+f'Аргументы функции: {args} {kwargs}\n'
            print(log)
            with open(path,'a', encoding = 'utf-8') as f:
                f.write(log)
            return result
        return create_log_string
    return __logger

log_path = 'hw_old.log'

@logger(log_path)
def get_link(keyword, snippet):
    if snippet.text.lower().find(keyword) >= 0:
        data = snippet.find('time').get('title')
        header = snippet.find('h2')
        header_span=''
        header_link=''
        if not header is None:
            header_span = header.find('span').text
            header_link = header.find('a').get('href')
        return f'{data}-{header_span}-{"https://habr.com" + header_link}'
    else:
        return ''


def main():
    url = 'https://habr.com/ru/all/'
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        all_snippets = soup.find_all(class_='article-snippet')
        for snippet in all_snippets:
            for keyword in KEYWORDS:
                result = get_link(keyword, snippet)
                if result:
                        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()