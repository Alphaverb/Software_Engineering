from random import *

def roll():
    num = randint(1, 6)
    print(f"Значение кубика: {num}")

    if num in [5, 6]:
        print("Вы победили")
    elif num in [3, 4]:
        print("Вы продолжаете игру...")
        roll()
    else:
        print("Вы проиграли")

if __name__ == "__main__":
    roll()