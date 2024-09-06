mi_dict = {'Max' : 1999, 'Duck' : 2009}
print(mi_dict)
print(mi_dict['Max'])
print(mi_dict.get('John'))
mi_dict.update({'Anna' : 1987, 'Kate' : 1977})
print(mi_dict)
a = mi_dict.pop('Anna')
print(a)
print(mi_dict)

mi_set = {1 , 2 , 2 , 1 , 'Melon' , 'Melon' , 3.14 , 42.342 }
print(mi_set)
mi_set.add(5)
mi_set.add(7)
mi_set.remove(42.342)
print(mi_set)
