import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()
result = translator.translate("dog", dest="ru")
print(result.text)


def get_english_worlds():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_worlds = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_words": english_worlds,
            "word_definition": word_definition
        }
    except Exception as e:  # Добавлено уточнение для обработки исключений
        print("Произошла ошибка:", e)


def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_worlds()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Ответ верный")
        else:
            print(f"Ответ неверный, было загадано слово - {word}")

        play_again = input("Хотите сыграть еще раз? (Y/N) ")
        if play_again.upper() != "Y":  # Проверка на регистр для 'Y'
            print("Спасибо за игру!")
            break


word_game()

