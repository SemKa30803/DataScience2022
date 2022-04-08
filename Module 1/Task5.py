ids = {'user1': [213, 213, 213, 15, 213],
'user2': [54, 54, 119, 119, 119],
'user3': [213, 98, 98, 35]}

a = []
for i in list(ids.values()):
    a+=i
print(' '.join(map(str,list(set(a)))))

