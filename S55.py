list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

def generate_set(list):
    index = 0
    while index < len(list):
        num_count = list.count(list[index])
        if num_count > 1:
            list[index] = str(list[index]) * num_count
        index += 1
    return set(list)

print("1-ый список: ", generate_set(list_1),
      "\n2-ой список: ", generate_set(list_2),
      "\n3-ий список: ", generate_set(list_3))
