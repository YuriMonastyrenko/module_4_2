def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function() # Печатает "Я в области видимости функции test_function"

inner_function() # Выдает ошибку "NameError: name 'inner_function' is not defined."
# вследствие различия пространства имён, т.к.  мы не можем доставать значения внутри функции (извне)

