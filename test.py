def capitalize(source_string):
    words = source_string.split(' ')
    print(words)
    words = [word.title() for word in words]
    print(words)
    result_string = ' '.join(words)
    return result_string



my_text = input('Введите текст: ')
capitalize(my_text)

