import math

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def percent(x, percent):
    return (percent / 100) * x

def step(x, exponent):
    return x ** exponent

def logarithm(x, base=math.e):
    if x <= 0:
        return "Ошибка: логарифм не определён для неположительных чисел!"
    return math.log(x, base)

def factorial(n):
    if n < 0:
        return "Ошибка: факториал не определён для отрицательных чисел!"
    return math.factorial(n)

if __name__ == "__main__":
    print("Базовые операции:")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", minus(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
    print("20% от 100 =", percent(100, 20))
    print("2 в степени 3 =", step(2, 3))
    print("Логарифм 100 по основанию 10 =", logarithm(100, 10))
    print("Факториал 5 =", factorial(5))
