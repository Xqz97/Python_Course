# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает). 

def sum_of_divisors(input_num: int):
    sum_1 = 0
    for i in range(1, input_num // 2 + 1):
        if input_num % i == 0:
            sum_1 += i
    return sum_1

def friendly_num(input_num: int):
    find_couple = set()
    for i in range (1, input_num + 1):
        sum_temp = sum_of_divisors(i)
        sum_2 = sum_of_divisors(sum_temp) 
        if sum_2 == i and sum_temp !=i and i not in find_couple and sum_temp not in find_couple:
            print(sum_temp, i)
            find_couple.add(i)
input_num = int(input("Введите число к: "))

friendly_num(input_num)