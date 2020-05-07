# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

# .isdigit() - проверка на int возращяет True/False isinstance - проверка на экземпляр принадлежности класса(float,str)
# и другие, сделано для того чтобы пользователь вводил те данные которые мы ожидаем

var_1 = 1
var_2 = "foobar"
print(var_1, var_2)

while True:
    var_num_1 = input("Введите число №1: ")
    var_num_2 = input("Введите число №2: ")

    if var_num_1.isdigit() and var_num_2.isdigit():
        print("Вы ввели:", var_num_1, var_num_2)
        break
    else: print("Одно или несколько введенных вами значений не число, Введите число")

while True:
    var_str_3 = input("Введите строку: ")
    var_str_4 = input("Введите строку: ")
    if  isinstance(var_str_3, str) and  isinstance(var_str_4, str):
        print("Вы ввели:", var_str_3, var_str_4)
        break
    else: print("Одно или несколько введенных вами значений не строка, Введите строку")
