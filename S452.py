from S451 import calculate

if __name__ == '__main__':
    a = float(input("Введите длину первой стороны треугольника: "))
    b = float(input("Введите длину второй стороны треугольника: "))
    c = float(input("Введите длину третьей стороны треугольника: "))

    result = calculate(a, b, c)

    print(f"Площадь треугольника с заданными сторонами равна: {result}")