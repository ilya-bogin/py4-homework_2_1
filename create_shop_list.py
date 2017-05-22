
def read_recipe_name(file):
  return file.readline().rstrip('\n').lower()


def read_ingridients_count(file):
  return int(file.readline())


def read_ingridients(file, ingridients_count):
  ingridients = []
  for i in range(ingridients_count):
    splitted_data = file.readline().rstrip('\n').split(" | ")

    if len(splitted_data) != 3:
      print('Wrong ingridients format')
      return

    ingridient = {
      'ingridient_name' : splitted_data[0],
      'quantity' : int(splitted_data[1]),
      'measure' : splitted_data[2],
    }
    ingridients.append(ingridient)
  return ingridients


def read_all_recipes_from_file(file_name):
  recipes = {}
  with open(file_name, newline='') as file:
    while True:
      recipe_name = read_recipe_name(file)
      if len(recipe_name) == 0:
        break;
      ingridients_count = read_ingridients_count(file)
      ingridients = read_ingridients(file, ingridients_count)
      recipes[recipe_name] = ingridients
  return recipes


def get_shop_list_by_dishes(cook_book, dishes, person_count):
  shop_list = {}
  for dish in dishes:
    if dish not in cook_book:
      print('Блюдо {} не найдено'.format(dish))
      continue
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  recipes = read_all_recipes_from_file('recipes.txt')
  print('Доступные блюда:')
  for recipe_name in recipes.keys():
    print(recipe_name)
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(recipes, dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()
