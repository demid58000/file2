from pprint import pprint

cook_book = {}
lst = ['ingredient_name', 'quantity', 'measure']
with open('text1', 'r', encoding = 'utf-8') as infile:
    file = infile.read().split('\n\n')
    for dishes in file:
        dishes = dishes.split('\n')
        cook_book[dishes[0]] = []
        for i in range(2, len(dishes)):
            ingredient = dishes[i].split(' | ')
            ingredient[1] = int(ingredient[1])
            cook_book[dishes[0]].append(dict(zip(lst, ingredient)))

def get_shop_list_by_dishes(dishes, person_count):
    cook_book2 = {}
    for dish in dishes:
        for i in range(len(cook_book[dish])):
            ingredient_name = cook_book[dish][i]['ingredient_name']
            if ingredient_name not in cook_book2:
                cook_book2[ingredient_name] = {}

                cook_book2[ingredient_name]['measure'] = cook_book[dish][i]['measure']
                cook_book2[ingredient_name]['quantity'] = cook_book[dish][i]['quantity'] * person_count
            else:
                cook_book2[ingredient_name]['quantity'] += cook_book[dish][i]['quantity'] * person_count
    








# print(cook_book['Омлет'])
# print(cook_book['Омлет'][1])
# print(cook_book['Омлет'][1][])
get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)



