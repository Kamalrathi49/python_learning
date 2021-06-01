from translate import Translator

try:
    with open('text.txt', mode='r') as my_file:
        text = my_file.read()
        translator = Translator(to_lang="ja")
        translation = translator.translate(text)
        print(f"english: {text} || japanese: {translation}")
        with open("text_file.txt", mode="w") as td_file:
            td_file.write(translation)
except IOError as e:
    print("there is an file error")
