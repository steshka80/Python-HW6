# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

my_list=[5, 4 , -17, 41, 0, 99, -27, 6, 23]
new_result = [my_list[i]*my_list[len(my_list)-1-i] for i in range((len(my_list) // 2)+1)]
print (new_result)