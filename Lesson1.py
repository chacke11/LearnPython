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

#def get_summ(one, two, delmiter = '&'):
 #   one = str(one)
  #  two = str(two)
   # delmiter = str(delmiter)
    #final = one + delmiter + two
    #return(final)


#a = get_summ('Learn','Python')
#print(a.upper())


#def format_price(price):
  #  price = int(price)
  #  price_new = f'Цена {price} руб.'
  #  return(price_new)

#b = format_price
#print(b)


#age = int(input(' Введите свой возраст: '))

#def age_init(age):
 #   if age <= 7:
  #      param = 'Детский сад'
   # elif age <= 17:
    #    param = 'Школа'
    #else:
   #     param = 'Вуз'
   # return (param)
#b = age_init(age)
#print(b)



def check_str(string1,string2):

    if string1 and string2 == str:
         result = 0
  
            
    elif string1 == string2:
       result = 1
        
                

    elif string1 != string2 and string1 > string2:
         result = 2
            
    elif string1 != string2 and string2 == 'Learn':
        result = 3
                
                
    return (result)

result = check_str('строка','строка')
print(result)

