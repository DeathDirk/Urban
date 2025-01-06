def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function() # ничего не произошло

#inner_function() #name 'inner_function' is not defined. Did you mean: 'test_function'?
# не выполняется потому что inner_function cуществует внутри test_function(а она не запущена) и пока не существует

test_function() #здесь всё отлично работает


# 1 Создайте новый проект в PyCharm
# 2 Запустите созданный проект
# Ваша задача:
# 1 Создайте новую функцию test_function
# 2 Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение
# "Я в области видимости функции test_function"
# 3 Вызовите функцию inner_function внутри функции test_function
# 4 Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы