# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты
# для них новыми партами. За каждой партой может
# сидеть два учащихся. Известно количество учащихся
# в каждом из трех классов. Выведите наименьшее число
# парт, которое нужно приобрести для них.

a = int(input("Введите количество учащихся в 1 классе \n"))
b = int(input("Введите количество учащихся в 2 классе \n"))
c = int(input("Введите количество учащихся в 3 классе \n"))

print((-(-a // 2)) + (-(-b // 2)) + (-(-c // 2)))