# """Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество
# элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится
# число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из
# целых чисел."""

n =  int(input("Введите сколько чисел в массиве: "))
n_1 = []
for i in range(n):
    n_2 = input("Введите числа в массиве: ")
    n_1.append(n_2)

count = 0
for i in range(1, len(n_1)-1):

    if (n_1[i] > n_1[i-1]) and (n_1[i] > n_1[i+1]):
        count+=1
    i+=1

print(count)
    