def thesaurus_avd(*args):
    fn_ln_sort = {}
    for fn_ln in args:
        fn_ln_sort.setdefault(fn_ln.split()[1][0], {}).setdefault(fn_ln.split()[0][0], []).append(fn_ln)
    return fn_ln_sort


print(thesaurus_avd('Иван Сергеев', 'Инна Серова', 'Иван Алексеев', 'Борис Серов', 'Алексей Иванов',
                    'Павел Борисов', 'Евгений Родионов', 'Жанна Родионова', 'Оксана Борисова'))