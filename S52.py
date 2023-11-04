results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9,
           27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = sorted(results)
best = sorted_results[:3]
worst = sorted_results[-3:]
begin_with_10 = sorted_results[9:]
print("Список результатов по возрастанию:", sorted_results,
      "\nТри лучших результата: ", best,
      "\nТри худших результата: ", worst,
      "\nРезультаты, начиная с 10: ", begin_with_10)


