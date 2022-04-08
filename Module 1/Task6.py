queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт',
]
dic = {}
for i in queries:
    num = len(i.replace(',',' ').replace('!',' ').replace('.',' ').replace('?',' ').split(' '))
    if num in dic.keys():
        dic[num] += 1
    else:
        dic[num] = 1

for i in sorted(dic):

    print('Поисковых запросов, содержащих {} слов(а): {}%'.format(i,round(dic[i]/len(queries)*10000)/100))
