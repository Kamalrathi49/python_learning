from translate import Translator

try:
    with open('text.txt', mode='r') as ts_file:
        text = ts_file.read()
        translator = Translator(to_lang="ja")
        translator2 = Translator(to_lang="zh")
        translation = translator.translate(text)
        translation2 = translator2.translate(text)
        print(translation)
        print(translation2)
        print(text)
except IOError as e:
    print("there is an file error")
