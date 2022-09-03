"""
2.	Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой
строке.
"""
with open(r"additionally/for_l52.txt", encoding='utf') as f_obj:
    content = f_obj.readlines()
    f_obj.seek(0)
    print(f'Всего строк: {len(content)}.')
    for i, j in enumerate(f_obj):
        print(f'В строке {i + 1} количество слов: {len(j.split()) }.')

