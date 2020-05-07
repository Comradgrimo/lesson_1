# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
while True:
    try:
        number = int(input("Введите число: "))
        break
    except ValueError:
        print("Введите число")

answer = int(number*2) + int(number*3) + int(number)
print(f"Считаем {number} + {number*2} + {number*3} = {answer}")