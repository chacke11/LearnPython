a = 2 
c = 10
d = 3
print('Hello World!')
print(a + a)
print(c / d) 
#===================

v = int(input('Введите число от 1 до 10: '))
print(v + 10 ) 

#===================

name = input('Введите ваше имя: ').upper()
print(f'Привет {name}! Как дела?')

#===================

print(float('1'))
print(int('2')) #Если оставить 2.5 будет ошибка
print(bool(1))
print(bool(''))
print(bool(0))

#===================

lists = [3,5,7,9,10.5]
print(lists)
lists.append('Python') # Добавляем в список
print ('Длина списка - ', len(lists)) # Выводим длину списка
print(lists[0])  # Выводим 1 ый элемент списка
print(lists[-1]) # Выводим последний элемент
print(lists[1:4]) #Выводим со второго по четвертый включительно
del lists[-1] # Удаляем по индексе
lists.remove('Python') # Удаляем по значению
print(lists)

#===================

weather = {"city": "Москва", "temperature": '20'}
print(weather['city'])
temp = int((weather['temperature']))
temp -= 5
weather['temperature'] = temp
print(weather)
weather.get('country', 'Россия')
weather['date'] = "27.05.2019"

print(weather)

#===================

def get_summ(one, two, delmiter = '&'):
    one = str(one)
    two = str(two)
    delmiter = str(delmiter)
    final = one + delmiter + two
    return(final)


a = get_summ('Learn','Python')
print(a.upper())

#===================


def format_price(price):
    price = int(price)
    price_new = f'Цена {price} руб.'
    return(price_new)

b = format_price
print(b)
#===================


string_1 = 'строка'
string_2 = 'Learn'

def comparison(string_1,string_2):
    if isinstance(string_1, str) and isinstance(string_1,str):
        print('0')
    else:
        pass 
    if string_1 == string_2:
        print('1')
    else:
        pass
    if string_1 != string_2 and string_1 > string_2:
        print('2')
    else:
        pass
    if string_1 != string_2 and string_2 == 'Learn':
        print('3')
    else:
        pass    

print(comparison(string_1,string_2))

#===================


age = int(input('Введите свой возраст - : '))

def your_age(age):
    if age <= 7:
        print("Детский сад")
    if age > 7 and age < 17:
        print('Школа')
    if age > 17:
        print('Вуз')

print(your_age(age))

#===================

temp = '1,2,3,4,5,6,7,8,9,10' # Список 10 целых чисел
temp = temp.split(',') #Убираем запятые 

for temp_new in temp:
    temp_new = (int(temp_new) + 1) #Перевели в инт и прибавили 1
    print(temp_new)



#===================



user = input('Введите любое предложение - : ')
for usr in user:
    print(usr) # Выводим по одному символу



#===================

def hello_user(a = input('Как дела? ')):
    while a != 'Хорошо':
        print('Должно быть хорошо!')
        a = input('Как дела? ')
        return a

print(hello_user())

#===================

dct = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
score = 5
def ask_user():
    while score > 0:
        qst = input('Задай вопрос - ')
        x = dct[qst]
        print (x)

print(ask_user())

#===================