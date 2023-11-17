import csv

def load_data():
    with open('expenses.csv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def save_data(data):
    fieldnames = ['№', 'Дата', 'Категория', 'Содержание операции', 'Расходы']
    with open('expenses.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_expense(data):
    if data:
        num = len(data) + 1
    else:
        num = 1

    date = input("Введите дату: ")
    category = input("Введите категорию: ")
    detail = input("Введите содержание операции: ")
    spent = input("Введите потраченную сумму: ")

    expense = {'№': num, 'Дата': date, 'Категория':  category, 'Содержание операции':  detail, 'Расходы': spent}
    return expense

def delete_expense(data, expense_num):
    for expense in data:
        if int(expense['№']) == expense_num:
            data.remove(expense)
            return True
    return False

def show_expenses(data):
    if not data:
        print("Нет сохраненных расходов.")
    else:
        print("Список расходов:")
        for expense in data:
            print(f"{expense['№']} | {expense['Дата']}: \n {expense['Категория']} — {expense['Содержание операции']} \n ({expense['Расходы']})")

if __name__ == "__main__":
    expenses = load_data()

    while True:
        print("\n1. Добавить расходы")
        print("2. Удалить расходы")
        print("3. Показать расходы")
        print("4. Выход")

        choice = input("\nВыберите действие (1/2/3/4): ")

        if choice == '1':
            expense = add_expense(expenses)
            expenses.append(expense)
            save_data(expenses)
            print("Расход успешно добавлен.")

        elif choice == '2':
            show_expenses(expenses)
            del_num = input("\nВведите номер расхода для удаления: ")
            if delete_expense(expenses, int(del_num)):
                save_data(expenses)
                print("Расход успешно удален.")
            else:
                print("Расход с указанным номером не найден.")

        elif choice == '3':
            show_expenses(expenses)

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")



