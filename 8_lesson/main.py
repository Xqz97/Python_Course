
import functions

while True:
    print('1.вывод, 2. добавление, 3. поиск, 4. удаление, 5. изменение')
    mode = int(input())
    if mode == 1:
        functions.show_data()
    elif mode == 2:
        functions.add_data()
    elif mode == 3:
        functions.find_data()
    elif mode == 4:
          functions.rem_data()
    elif mode == 5:
        functions.change_data()
    else:
        break

