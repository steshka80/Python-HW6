# Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности.
#Пример:
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

list_numb = [1, 2, 3, 5, 1, 5, 3, 10]
list_result = [list_numb[i] for i in range(len(list_numb)) if list_numb[i] not in list_numb[list_numb[i]:]]
print(list_result)
