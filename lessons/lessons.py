n = int(input('Введите кол-во уроков: '))
sum = 0  # счетчик нечетных уроков
sum1 = 0  # счетчик четных
for i in range(1, n + 1, 2):
    sum += 1
    a = sum * 5  # кол-во перемен по 5
for x in range(1, n, 2):
    sum1 += 1
    b = sum1 * 15  # кол-во перемен по 15
if n % 2 == 0:
    b = b - 15  # если последний урок четный
else:
    a = a - 5  # если последний урок нечетный
time_out = n * 45 + a + b  # время змнятий с переменами
end_hour = time_out // 60  # время змнятий часы
end_minut = time_out % 60  # время змнятий минуты
endlesson_h = 8 + end_hour
endlesson_m = end_minut

print('Уроки завершатся в ', endlesson_h, 'часов', endlesson_m, 'минут')
