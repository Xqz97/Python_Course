# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (
#     т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение
# # Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#

l = input("Введите фразу: ")
l_1 = l.split()
print(l_1)

l_2 = [sum(x in 'уеыаоэяию' for x in lin) for lin in l_1]
print(l_2)

if len(set(l_2)) == 1:
    res = "Парам пам-пам"
else:
    res = "Пам парам"
print(res)

