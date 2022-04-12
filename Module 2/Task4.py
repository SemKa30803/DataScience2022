import numpy as np

users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ],
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])
coses = np.array([])
for user in users_stats:
    coses = np.append(coses, (np.dot(user, next_user_stats) / (np.linalg.norm(user) * np.linalg.norm(next_user_stats))))
print('Самый похожий пользователь: №{}, {}'.format(list(coses).index(max(coses)) + 1,
                                                   users_stats[list(coses).index(max(coses))]))
