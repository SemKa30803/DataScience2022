sum = 0
while True:
    n = int(input('Введите число\n'))
    if n == 0:
        print('Результат\n{}'.format(sum))
        break
    sum += n
