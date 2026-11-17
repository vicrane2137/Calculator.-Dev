print("Первое число: " )
a = int(input())
print("Второе число: ")
b = int(input())
print("Введите желаемое действие (+, -, /, *) ")
znak = input()
if znak == "+":
    print(a + b)
elif znak == "-":
    print(a - b)
elif znak == "*":
    print(a * b)
elif znak == "/":
    print(a / b)

#v2. Только сложение и вычитание. Калькулятор. Добавлены подсказки для пользователя
