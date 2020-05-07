# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
while True:
    try:
        number = int(input("Введите число: "))
        if number < 0:
            print("Введите целое положительное число")
        else:
            break
    except ValueError:
        print("Введите целое положительное число")

old_number = number
r=0
while number >= 1:
    d= number % 10
    number = number //10
    if d > r:
        r=d
print(f"Самая большая цифра в введенном Вами числе ({old_number}) - {r}")