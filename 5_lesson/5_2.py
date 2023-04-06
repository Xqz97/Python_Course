# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

def min_change_to_max(list):
    min = list[0]
    max = list[0]
    for i in range (len(list)):
        if list[i] > max:
            list[i] = max
        if list[i] < min:
            list[i] =  min
    for i in range (len(list)):
        if list[i] == max:
            list[i] = min

list_1 = []
list_len = int(input("Введите количество оценок: "))
for _ in range(list_len):
    list_1.append(int(input("Введите оценку: ")))
print(list_1)
print(min_change_to_max(list_1))
