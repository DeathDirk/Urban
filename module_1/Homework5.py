immutable_var = (True, 3, 'String', [5, 7])
print(immutable_var)
#immutable_var [0] = 1 #кортеж не поддерживает изменение своих элементов но может содержать в себе изменяемые элементы
mutable_list = ['String', 15, True]
mutable_list [0] = 4
mutable_list.append('Modified')
print(mutable_list)
mutable_list.extend(['Fire'])
print(mutable_list)
mutable_list.remove('Modified')
print(mutable_list)
