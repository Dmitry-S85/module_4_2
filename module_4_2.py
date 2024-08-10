def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

# inner_function()
# при вызове функции inner_function() за пределами данной функции выдает ошибку,
# т.к. функция находится в другом пространстве времен