boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

print('Идеальные пары\n'+'\n'.join([str(i)+' и '+str(j) for i, j in zip(sorted(boys), sorted(girls))]) if len(boys) == len(girls) else 'Внимание, кто-то может остаться без пары!')

