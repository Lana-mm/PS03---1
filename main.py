import requests
from bs4 import BeautifulSoup
from googletrans import Translator

translator = Translator()


def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except Exception as e:
        print("Произошла ошибка:", e)


def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и определение на русский
        translated_word = translator.translate(word, dest="ru").text
        translated_definition = translator.translate(word_definition, dest="ru").text

        print(f"Значение слова - {translated_definition}")
        user = input("Что это за слово? ")

        if user.lower() == translated_word.lower():
            print("Ответ верный")
        else:
            print(f"Ответ неверный, было загадано слово - {translated_word}")

        play_again = input("Хотите сыграть еще раз? (Y/N) ")
        if play_again.upper() != "Y":
            print("Спасибо за игру!")
            break

    word_game()

word_game()

