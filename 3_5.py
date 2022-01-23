from random import choice, randrange


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_joker(n, repaet=False):
    """

    Функция возвращает не повторяющиеся шутки, собранные из трех списков со словами

    """
    get_list = []
    list_min = min(nouns, adverbs, adjectives)
    while n and len(list_min):
        num = randrange(len(list_min))
        if repaet:
            get_list.append(f'{nouns.pop(num)} {adverbs.pop(num)} {adjectives.pop(num)}')
        else:
            get_list.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
        n -= 1
    return get_list


print(get_joker(n=int(input('Введите количество шуток: '))))

