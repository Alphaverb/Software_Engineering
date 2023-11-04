mark_list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
mark_list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
mark_list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def good_marks(list):
    updated_mark_list = [4 if mark == 3 else mark for mark in list if mark != 2]
    return updated_mark_list

print("Обновленный список оценок для первого варианта:", good_marks(mark_list1),
      "\nОбновленный список оценок для второго варианта:", good_marks(mark_list2),
      "\nОбновленный список оценок для третьего варианта:", good_marks(mark_list3))
