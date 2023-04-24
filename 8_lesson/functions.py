
import csv
def show_data():
    '''Выводит информацию из справочника'''
    with open('phonebook.csv', 'r', encoding= 'utf-8') as pb:
       a = csv.reader(pb, delimiter=' ', quotechar='|')
       for i in a:
            print(', '.join(i))

# _____________________________________________________________________________________________ 

def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО через пробел: ')
    tel = input('Введите телефон: ')
    with open('phonebook.csv', 'a', encoding= 'utf-8', newline= '') as pb:
         tpb = csv.writer(pb)
         tpb.writerow([fio, "|", tel])
    print('Операция выполнена успешно!')

# _____________________________________________________________________________________________ 


def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    with open('phonebook.csv', 'r', encoding= 'utf-8') as pb:
        tpb = pb.read()
        print(search(tpb, data).replace(",", " "))

def search(a: str, b: str) -> str:
    '''Находит записи по какому-либо критерию поиска'''
    a = a.split('\n')
    return '\n'.join([i for i in a if b in i])

# _____________________________________________________________________________________________ 

def change_data():
    """Изменяет данные в телефонном справочнике"""
    l = []
    with open('phonebook.csv', 'r', encoding='utf-8') as pb:
        for i, j in enumerate(csv.reader(pb), start= 1):
            print(i, *j)
            l.append(j)
        rd = int(input("Укажите номер строки с для изменений: "))
        if rd < 1 or rd > len(l):
            print("Строка отсутствует в спрачонике!")
            return
        l[rd-1] = [input("ФИО "), "|", input("Номер ")]
    with open('phonebook.csv', 'w', encoding='utf-8', newline='') as pb:
        tpb = csv.writer(pb)
        tpb.writerows(l)
# _____________________________________________________________________________________________ 
       
def rem_data():
    """Удаляест данные из справочника"""
    l = []
    with open('phonebook.csv', 'r', encoding='utf-8') as pb:
        for i, j in enumerate(csv.reader(q), start=1):
            print(i, *j)
            l.append(j)
        rd = int(input("Введите номер строки для удаления: "))
        if rd < 1 or rd > len(l):
            print("Строка отсутствует в справочнике!")
            return
        l.pop(rd-1)
    with open('phonebook.csv', 'w', encoding='utf-8', newline='') as pb:
        tpb = csv.writer(pb)
        tpb.writerows(l)