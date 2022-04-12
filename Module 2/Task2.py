import numpy as np

N = int(input('Введите N: '))
arr = np.diag(np.arange(N, 0, -1))
print('Матрица :\n', arr)
print('Сумма значений: ', np.sum(arr))
