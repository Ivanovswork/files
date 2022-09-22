def file(name_file):
    cook_book = {}
    with open(name_file, encoding="utf8") as f:
        while True:
            name = f.readline().strip()
            count = int(f.readline())
            cook_book[name] = []
            for i in range(count):
                bludo = {}
                row = f.readline().split(' | ')
                bludo['ingredient_name'] = row[0]
                bludo['quantity'] = int(row[1])
                bludo['measure'] = row[2].strip()
                cook_book[name].append(bludo)
            next_row = f.readline()
            if next_row != '\n':
                break
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    dict_of_measure = {}
    for bludo in dishes:
        ingredients = file('f.txt')[bludo]
        for elem in ingredients:
            ingredient = elem['ingredient_name']
            if ingredient in dict_of_measure.keys():
                dict_of_measure[ingredient]['quantity'] + elem['quantity'] * person_count
            else:
                dict_of_measure[ingredient] = {}
                dict_of_measure[ingredient]['measure'] = elem['measure']
                dict_of_measure[ingredient]['quantity'] = elem['quantity'] * person_count
    print(dict_of_measure)

get_shop_list_by_dishes(['Запеченный картофель', "Фахитос"], 2)