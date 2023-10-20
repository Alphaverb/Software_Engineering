vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
countV = 0

string = (input('Введите предложение на английском: '))
print('Длина предложения: ', len(string))
print('Предложение в нижнем регистре: ', string.lower())

for i in range(0, len(string)-1, 1):
    for j in range(0, len(vowels)-1, 1):
        if vowels[j] == string[i]:
            countV += 1
print(f"Количество гласных в предложении: {countV}")

if "ugly" in string:
    noUgly = string.replace("ugly", "beauty")
    print('Замена ugly на beauty: ', noUgly)

if string.startswith('The'):
    print('Строка начинается на The')
else:
    print('Строка не начинается на The')

if string.endswith('end'):
    print('Строка заканчивается на end')
else:
    print('Строка не заканчивается на end')

