import pprint

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        dish_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for n in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            ingridient, quantity, unit = recipe
            ingredients.append({'ingridient_name': ingridient, 'quantity': quantity, 'measure': unit})
        file.readline()
        cook_book[dish_name] = ingredients


def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingridient_name'] in result:
                    result[consist['ingridient_name']]['quantity'] += int(consist['quantity']) * person_count
                else:
                    result[consist['ingridient_name']] = {'measure': consist['measure'],
                                                          'quantity': (int(consist['quantity']) * person_count)}
        else:
            print('Такого блюда нет в книге')
    pprint.pprint(result)


get_shop_list_by_dishes(['Салат змейка', 'Фахитос'], 2)
