def slice(tuple, element):
    if element in tuple:
        if tuple.count(element) > 1:
            first = tuple.index(element)
            second = tuple.index(element, first + 1) + 1
            return tuple[first:second]
        else:
            return tuple[tuple.index(element):]
    else:
        return ()

print(slice((1, 2, 3), 8),
      slice((1, 8, 3, 4, 8, 8, 9, 2), 8),
      slice((1, 2, 8, 5, 1, 2, 9), 8), sep='\n')