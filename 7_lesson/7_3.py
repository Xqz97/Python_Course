# Задача на логику.

n = int(input())
some_list = []
for _ in range(2*n):
    temp_list = []
    for i in input().split:
        if i[-1] in ('1', '3'):
            temp_list.append(i)
    some_list.append(temp_list)

print(some_list)
for ind in range(0, len(some_list) - 1, 2):
    res = list(set(some_list[ind]).intersection(set(some_list[ind+1])))
    res = list(map(int, res))
    print(*sorted(res, reverse=True, sep= ' & '))