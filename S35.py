values = [0, 2, 4, 6, 8, 10]
counter = 0
string = 'hello'
memory = ' world'

while counter != 10:
    counter += 1
    if counter in values:
        print(string + memory)
        print(string)
string = string + ' world'
memory = string
print(memory)

