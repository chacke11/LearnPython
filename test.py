dct = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
score = 5
def ask_user():
    while score > 0:
        qst = input('Задай вопрос - ')
        x = dct[qst]
        print (x)

print(ask_user())

