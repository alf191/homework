import string

a = input('Введите пароль: ')

upper_1 = 0
lower_1 = 0
punctuation_1 = 0
number = 0
for i in a:
    if i.isupper():
        upper_1 = +1
    elif i.islower():
        lower_1 = +1
    elif i.isdigit():
        number = +1
    else:
        string.punctuation = +1
if len(a) < 10:
    print('Пароль должен иметь не менее 10 символов')
elif upper_1 >= 1 and lower_1 >= 1 and number >= 1 and string.punctuation >= 1:
    print('Пароль сильный')
else:
    print('Пароль слабый')
