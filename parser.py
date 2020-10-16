import requests
from bs4 import BeautifulSoup


def get_url_text(url):
    # возвращаемый список с текстом
    text_list = list()

    img_list = list()
    video_list = list()
    audio_list = list()
    href_dict = dict()  # словарь с ссылками
    url_list = list()

    tags_list = ['p', 'h', 'b', 'big', 'small', 'i', 'strong', 'sub', 'sup', 'ins', 'del', 'th']  # теги, содержащие текст

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ СОДЕРЖАЩИХ ТЕКСТ
    for elem in tags_list:
        for tag in soup.findAll(elem):
            if tag.string:
                strings = tag.string
                lines = strings.split('. ')
                for line in lines:  # это предложение
                    text_list.append(line)

    # ВЫТАСКИВАНИЕ ТЕКСТОВ ИЗ ТЕГОВ <h>
    for h in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        for tag in soup.findAll(h):
            text_list.append(tag.string)

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <a>
    for tag in soup.findAll('a'):
        if tag.string:
            href_dict[tag.string] = tag.get('href')

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <audio>
    for tag in soup.findAll('audio'):
        if tag:
            audio = BeautifulSoup(str(tag), 'html.parser')  # что бы искал внутри тега
            if tag.get('src'):
                audio_list.append(tag.get('src'))
            for source in audio.findAll('source'):  # для тега <source>
                if source and source.get('src'):
                    audio_list.append(source.get('src'))

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <video>
    for tag in soup.findAll('video'):
        if tag:
            video = BeautifulSoup(str(tag), 'html.parser')  # что бы искал внутри тега
            if tag.get('src'):
                video_list.append(tag.get('src'))
            for source in video.findAll('source'):   # для тега <source>
                if source and source.get('src'):
                    video_list.append(source.get('src'))

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <img>
    for img in soup.find_all('img'):
        try:
            alt = img.attrs['alt']
            if alt == '':  # для таких тегов как alt=""
                img_list.append(img.get('src'))
        except KeyError:  # на случай, если alt не существует
            img_list.append(img.get('src'))
        else:  # если существует
            href_dict[alt] = img.get('src')

    url_list.append(img_list)
    url_list.append(audio_list)
    url_list.append(video_list)

    # ВЫТАСКИВАНИЕ ТЕКСТА ИЗ ТЕГОВ <span>
    for span in soup.find_all('span'):
        text_list.append(span.string)

    return text_list, href_dict, url_list


def print_text(url):
    text, href, urls = get_url_text(url)

    print('\n\n\t\t\t\t\t__________ТЕКСТ_________\n\n')  # отделение текста от ссылок

    for elem in text:  # вывод текста
        print(elem)

    print('\n\n\t\t\t\t\t__________ССЫЛКИ_________\n\n')  # отделение ссылок от текста

    for key, value in href.items():  # вывод ссылок
        print(f'{key}: {value}')

    print('\n\n\t\t\t\t\t__________ИЗОБРАЖЕНИЯ_________\n\n')

    for elem in urls[0]:
        print(elem)

    print('\n\n\t\t\t\t\t__________АУДИО_________\n\n')

    for elem in urls[1]:
        print(elem)

    print('\n\n\t\t\t\t\t__________ВИДЕО_________\n\n')

    for elem in urls[2]:
        print(elem)

def start():

    while True:  # для парсинга нескольких страниц не закрывая
        answer = input('Включить парсер(y or n)? ')
        if answer == 'y':
            url = input('url: ')
            text = print_text(url)
        else:
            break


if __name__ == '__main__':
    start()  # включение
