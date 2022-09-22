def sorting(list_of_files, result_file):
    list_of_raws = {}
    max_len = 0
    min_len = 10*1000000000000000000000000000000000000
    for elem in list_of_files:
        with open(elem, encoding='utf8') as file:
            f = file.read().split('\n')
            list_of_raws[file.name] = f
            if len(f) > max_len:
                max_len = len(f)
            if len(f) < min_len:
                min_len = len(f)
    print(min_len, max_len)
    print(list_of_raws)
    with open(result_file, 'a', encoding='utf8') as file:
        for i in range(min_len, max_len + 1):
            for elem in list_of_raws.keys():
                if len(list_of_raws[elem]) == i:
                    file.writelines(elem + '\n')
                    file.writelines(str(len(list_of_raws[elem])) + '\n')
                    for el in list_of_raws[elem]:
                        file.writelines(el + '\n')
k = ['1.txt', '2.txt', '3.txt']
sorting(k, 'res.txt')
# файл res обязательно должен быть чист