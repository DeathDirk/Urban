first = int(input('Enter the first number '))
second = int(input('Enter the second number '))
third = int(input('Enter third number '))
list_ = [first, second, third]
set_ = set(list_)
if len(set_) == 3:
    print('Similar numbers ', 0)
elif len(set_) == 2:
    print('Similar numbers ', 2)
elif len(set_) == 1:
    print('Similar numbers ', 3)
