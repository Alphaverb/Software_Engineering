def sum_num():
    try:
        number = input("Введите число: ")
        result = 2 + float(number)
        print(f"Результат сложения: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

sum_num()
sum_num()
sum_num()
sum_num()
