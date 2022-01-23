num_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
          'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
          'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(num):
    if num.istitle():
        return str(num_dict.get(num.lower())).title()
    return num_dict.get(num)


print(num_translate(input('Введите число прописью на английском: ')))