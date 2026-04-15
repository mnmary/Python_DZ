import requests
from bs4 import BeautifulSoup


def main():

    KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'программисты']
    url = 'https://habr.com/ru/all/'
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        all_snippets = soup.find_all(class_='article-snippet')
        for snippet in all_snippets:
            for keyword in KEYWORDS:
                if snippet.text.lower().find(keyword) >= 0:
                    data = snippet.find('time').get('title')
                    header = snippet.find('h2')
                    if not header is None:
                        header_span = header.find('span').text
                        header_link = header.find('a').get('href')
                    print(f'{data}-{header_span}-{"https://habr.com" + header_link}')
    except Exception as e:
        print(e)
if __name__ == '__main__':
    main()
