def remove(tuple, element):
    if element in tuple:
        index = tuple.index(element)
        new_tuple = tuple[:index] + tuple[index + 1:]
        return new_tuple
    else:
        return tuple

print(remove((1, 2, 3), 1),
      remove((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
      remove((2, 4, 6, 6, 4, 2), 9), sep='\n')
