with open('input.txt', encoding='utf-8') as f:
    data = f.read()

    excluded = [' ', '\n', '.']
    count = 0
    for letter in data:
        if letter not in excluded:
            count += 1
    letters = count

    words = len(data.split())
    lines = len(data.split('\n'))

print(f"Input file contains:\n{letters} letters\n{words} words\n{lines} lines")
