str = []
for readLine in open("recipes.txt", encoding="utf-8"):
    str.append(readLine)

#1
cook_book = {}
while True:
    if len(str) == 0:
        break
    cook_bludo = {}
    bludo = str.pop(0)
    bludo = bludo[:-1]
    cook_bludo['name'] = bludo

    cnt_in_bludo = str.pop(0)

    ingredient1 = []

    while True:
        ingredient_dict = {}
        ingredient = str.pop(0)
        if ingredient == '\n':
            break
        if len(str) == 0:
            break
        ingredient_ = ingredient[:-1].split("|")
        ingredient_dict['ingredient_name'] = ingredient_[0].strip()
        ingredient_dict['quantity'] = int(ingredient_[1])
        ingredient_dict['measure'] = ingredient_[2].strip()

        ingredient1.append(ingredient_dict)

    cook_bludo['ingredient'] = ingredient1

    cook_book[cook_bludo['name']] = cook_bludo['ingredient']

#print(cook_book)

#2
def get_dish(dish_name):
    return cook_book[dish_name]

def get_shop_list_by_dishes(dishes, person_count):
    dishes_list = {}
    for dish in dishes:
        #print('\n', dish, '\n')
        dish_dict = get_dish(dish)
        #print(dish_dict)
        for ing in dish_dict:
            ing_name = ing['ingredient_name']
            ingredient_in_ingredientes = ing['ingredient_name'] in dishes_list

            if ingredient_in_ingredientes:
                dishes_list[ing_name]['quantity'] += ing['quantity']*person_count
            else:
                dishes_list[ing_name] = {}
                dishes_list[ing_name]['quantity'] = ing['quantity']*person_count
                dishes_list[ing_name]['measure'] = ing['measure']

    return dishes_list

dishes = ['Омлет','Омлет']

print(get_shop_list_by_dishes(dishes, 2))