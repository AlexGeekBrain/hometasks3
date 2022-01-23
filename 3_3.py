name = ["Иван", "Мария", "Петр", "Илья", 'Алексей']


def thesaurus():
    name_dict = {}
    for i in sorted(name):
        if i[0] in name_dict.keys():
            name_dict[i[0]].append(i)
        else:
            name_dict[i[0]] = [i]
    return(name_dict)


print(thesaurus())