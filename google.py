from googletrans import Translator

translator = Translator()

def detecter(string):
    des='uz' if translator.detect(string).lang=='en' else 'en'
    return des


def self_translator(string):
    des = detecter(string)
    out = translator.translate(string, des).text
    return out


if __name__ == '__main__':
    print(self_translator('Salom'))
