# Найдите сумму трехзначного числа


# Решил попробовать сделать через строки, так как такая задача через математику уже была у нас в С#
a = input("Введите число: \n")
if len(a) != 3:
    print("Число не трехзначное: ")
else:
    b = list(map(int, list(a))) #Прочитал про функцию map(), которая применяет действие к каждому элементу.
    c = b[:3]
    s = sum(c) # Также узнал о функции sum(), суммирующей все в нужном диапазоне.
    print(f"Сумма равна: {s}")