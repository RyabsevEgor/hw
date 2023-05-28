import collections
pets = {1:{"Мухтар": {"Вид питомца": "Собака","Возраст питомца": 9, "Имя владельца": "Павел"},},
        2:{ "Каа": {"Вид питомца": "желторотый питон","Возраст питомца": 19,"Имя владельца": "Саша"},},
    # и так далее
}

def create():
  data = {}
  last = collections.deque(pets, maxlen=1)[0]
  print('введите имя питомца')
  pet_name = input()
  print('введите вид питомца')
  vid = input()
  print('введите возраст питомца')
  age = input()
  print('введите имя владельца')
  owner = input()
  data = {"Вид питомца":vid,"Возраст питомца": age,"Имя владельца": owner}
  pet_data = {pet_name:data}
  pets[last+1] = pet_data

def get_pet(ID):
  return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
  age = int(age)
  if age % 10 == 1:
    age_ending = 'год'
  elif 1 < age % 10 < 5:
    age_ending = 'года'
  elif 4 < age % 10 < 10:
    age_ending = 'лет'
  return age_ending

def read(ID):
  if ID in pets.keys():
    name = list(get_pet(ID).keys())[0]
    print('Это', get_pet(ID)[name]["Вид питомца"], 
        list(get_pet(ID).keys())[0]+'.', 'Возраст питомца:', 
        str(get_pet(ID)[name]["Возраст питомца"]), 
        get_suffix(get_pet(ID)[name]["Возраст питомца"]) + 
        '.', 'Имя владельца:', get_pet(ID)[name]["Имя владельца"])
  else:
    print('Такой записи нет')

def update():
  print('введите ID')
  ID = int(input())
  data = {}
  print('введите имя питомца')
  pet_name = input()
  print('введите вид питомца')
  vid = input()
  print('введите возраст питомца')
  age = input()
  print('введите имя владельца')
  owner = input()
  data = {"Вид питомца":vid,"Возраст питомца": age,"Имя владельца": owner}
  pet_data = {pet_name:data}
  pets[ID] = pet_data

def delete():
  ID = print('введите ID')
  pets.pop(ID,"Такой записи нет")

def pets_list():
  for key in pets:
    read(key)
command =''
while command != 'stop':
  print('','для создания новой записи введите     create',
      'для обновления записи введите         update',
      'для чтения записи по ID введите       read',
      'для вывода всего словаря введите      print list',
      'для выхода введите                    stop', '', sep = ('\n'))
  command = input()
  if command == 'create':
    create()
  elif command == 'update':
    update()
  elif command == 'delete':
    delete()
  elif command == 'read':
    print('введите ID')
    ID = int(input())
    read(ID)
  elif command == 'print list':
    pets_list()
  elif command != 'stop':
    print('ошибка, такой команды нет')