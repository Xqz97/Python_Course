#  Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X

n = int(input("Введите количество элементов в массиве: "))

l_1 = list(map(int, input("Введите список чисел, разделенных пробелом: ").split()))
print("Список чисел: ", l_1)

x = int(input("Введите число для поиска: "))

print(f"Число встречается: {sum([1 for i in range(n)  if l_1[i] == x])} раз или раза")