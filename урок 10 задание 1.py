pets = {}
print('введите имя питомца')
pet_name = input()
print('введите вид питомца')
vid = input()
print('введите возраст питомца')
age = int(input())
print('введите имя владельца')
owner_name = input()

data = {'Вид питомца': vid, 'Возраст питомца': age,
          'Имя владельца': owner_name}
pets[pet_name] = data

if int(data['Возраст питомца'])%10 == 1:
  age_ending = 'год'
elif 1 < int(data['Возраст питомца'])%10 < 5:
  age_ending = 'года'
elif 4 < int(data['Возраст питомца'])%10 < 10:
  age_ending = 'лет'

for key in pets.keys():
   name = (key)

print('Это', pets[name]['Вид питомца'], 'по кличке', '"' + name
+ '".','Возраст питомца:', str(pets[name]['Возраст питомца']), age_ending
+ '.', 'Имя владельца:', pets[name]['Имя владельца'])