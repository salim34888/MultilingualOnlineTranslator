import requests
from bs4 import BeautifulSoup
phrases_list = []
word_list = []
find_all = 'not_all'
languages = {1: "arabic", 2: "german", 3: "english", 4: "spanish", 5: "french", 6: "hebrew", 7: "japanese",
             8: "dutch", 9: "polish", 10: "portuguese", 11: "romanian", 12: "russian", 13: "turkish"}
urls = []
y_l, l_t = '', ''


class Translator:
    def __init__(self):
        super().__init__()

    def get_input(self):
        global languages, y_l, l_t, all_languages, find_all
        y_l = int(input())
        print("Type the number of a language you want to translate to or '0' to translate to all languages:")
        l_t = int(input())
        your_language = dict.setdefault(languages, y_l)
        translate_to = dict.setdefault(languages, l_t)

        if l_t == 0:
            languages.pop(y_l)
            translate_to = "all"

        word = input('Type the word you want to translate:\n')

        return your_language, translate_to, word

    def create_url(self, your_language, translate_to, word):
        global all_languages, find_all, urls
        url = ''
        url = f'https://context.reverso.net/translation/{your_language}-{translate_to}/{word}'
        return url

    def get_synonym_words(self, soup):
        divs = soup.find('div', {'id': 'translations-content'})
        word_list = divs.text
        word_list = word_list.split()
        return word_list

    def get_examples(self, soup):
        sections = soup.find('section', {'id': 'examples-content'})
        phrases_list = []

        for span in sections.find_all('span', {'class': 'text'}):
            phrases_list.append(span.text.strip())
        return phrases_list

    def main(self):
        global word_list, phrases_list, urls, find_all

        your_language, translate_to, word = self.get_input()
        all_languages = []

        if translate_to == "all":
            for i in languages.values():
                all_languages.append(i)
            index1 = 0
            for i in range(12):
                translate_to = all_languages[index1]
                url = self.create_url(your_language, translate_to, word)

                r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(r.content, 'html.parser')

                divs = soup.find('div', {'id': 'translations-content'})
                word_list = divs.text
                word_list = word_list.split()

                phrases_list = self.get_examples(soup)

                print(f"{all_languages[index1]} Translations:")
                check = 0
                for i in word_list:
                    if check == 1:
                        break
                    print(i)
                    check += 1

                check = 0
                print(f"{all_languages[index1]} Examples:")
                for i in phrases_list:
                    if check == 2:
                        break
                    print(i)
                    check += 1
                index1 += 1
            print()
            exit()

        else:
            url = self.create_url(your_language, translate_to, word)

            r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(r.content, 'html.parser')

            word_list = self.get_synonym_words(soup)
            phrases_list = self.get_examples(soup)

            print(f"{translate_to} Translations:")
            check = 0
            for i in word_list:
                if check == 5:
                    break
                print(i)
                check += 1
            print()
            check = 0
            print(f"{translate_to} Examples:")
            for i in phrases_list:
                if check == 10:
                    break
                print(i)
                check += 1

print("""
Hello, welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish
Type the number of your language:""")

translator = Translator()
if __name__ == '__main__':
    translator.main()

languages = {1: "Arabic", 2: "German", 3: "English", 4: "Spanish", 5: "French", 6: "Hebrew", 7: "Japanese",
             8: "Dutch", 9: "Polish", 10: "Portuguese", 11: "Romanian", 12: "Russian", 13: "Turkish"}

translate_to2 = dict.setdefault(languages, l_t)
