import numpy as np

coefs = np.array([[4, 2, 1], [1, 3, 0], [0, 5, 4]])
vals = np.array([4, 12, -3])
ans = np.linalg.solve(coefs, vals)
print('x={}, y={}, z={}'.format(round(ans[0] * 100) / 100, round(ans[1] * 100) / 100, round(ans[2] * 100) / 100))
