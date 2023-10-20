string = 'КОТ'
index = len(string) - 1
for i in range(index, -1, -1):
    word = string[index]
    print(word, index)
    index -= 1
