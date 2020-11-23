#a = 2 
#c = 10
#d = 3
#print('Hello World!')
#print(a + a)
#print(c / d) 
#===================

#v = int(input('Введите число от 1 до 10: '))
#print(v + 10 ) 

#===================

#name = input('Введите ваше имя: ').upper()
#print(f'Привет {name}! Как дела?')

#===================

#print(float('1'))
#print(int('2')) #Если оставить 2.5 будет ошибка
#print(bool(1))
#print(bool(''))
#print(bool(0))

#===================

#lists = [3,5,7,9,10.5]
#print(lists)
#lists.append('Python') # Добавляем в список
#print ('Длина списка - ', len(lists)) # Выводим длину списка
#print(lists[0])  # Выводим 1 ый элемент списка
#print(lists[-1]) # Выводим последний элемент
#print(lists[1:4]) #Выводим со второго по четвертый включительно
#del lists[-1] # Удаляем по индексе
#lists.remove('Python') # Удаляем по значению
#print(lists)

#===================

#weather = {"city": "Москва", "temperature": '20'}
#print(weather['city'])
#temp = int((weather['temperature']))
#temp -= 5
#weather['temperature'] = temp
#print(weather)
#weather.get('country', 'Россия')
#weather['date'] = "27.05.2019"

#print(weather)

#===================

def get_summ(one, two, delmiter = '&'):
    one = str(one)
    two = str(two)
    delmiter = str(delmiter)
    final = one + delmiter + two
    return(final)


a = get_summ('Learn','Python')
print(a.upper())


def format_price(price):
    price = int(price)
    price_new = f'Цена {price} руб.'
    return(price_new)

b = format_price
print(b)

def capitalize(source_string):
    words = source_string.split(' ')
    print(words)
    words = [word.title() for word in words]
    print(words)
    result_string = ' '.join(words)
    return result_string