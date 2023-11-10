def count(list):
    num_dict = {int(num): list.count(num) for num in list}
    sort_list = sorted(num_dict.items(), key=lambda element: element[1])
    return dict(sorted(sort_list[-3:]))

print(count('145388198200163'),
      count('565992201820173'),
      count('293001198219401'), sep='\n')
