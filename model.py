import database as db
print("Информационная система на основе базы SQLite\n")
db.create_db()
db.create_table()
print("Список доступных команад: \n"
                                   "*Добавить данные\n"
                                   "*Показать данные в таблице\n"
                                   "*Найти данные по значению в таблице\n"
                                   "*Изменение данных\n"
                                   "*Удаление данных\n")

print("Список доступных таблиц: \n"
                                   "*cars\n"
                                   "*sports_cars\n"
                                   "*trucks\n")
while True:
    command = input("Введите команду: ")

    if command == "Добавить данные":
        table = input("Введите наименование таблицы для введения данных: ")
        name = input("Введите наименование автомобиля: ")
        year_of_manufacture = input("Введите год выпуска автомобиля: ")
        mileage = input("Введите пробег автомобиля: ")
        color = input("Введите цвет автомобиля: ")
        engine_power = input("Введите мощность двигателя автомобиля: ")
        drive = input("Введите привод автомобиля: ")
        db.add_data_to_table(table, name, year_of_manufacture, mileage, color, engine_power, drive)

    elif command == "Показать данные в таблице":
        table = input("Введите название таблицы: ")
        db.show_data(table)

    elif command == "Найти данные по значению в таблице":
        table = input("Введите название таблицы: ")
        column = input("Введите наименование колонки таблицы: ")
        value = input("Введите искомое значение: ")
        db.find_data_value(table, column, value)

    elif command == "Изменение данных":
        table = input("Введите название таблицы: ")
        value2 = input("Введите наименование машины в которой хотите поменять данные: ")
        column1 = input("Введите наименование колонки, значение которое нужно изменить: ")
        value1 = input("Введите новое значение: ")
        db.data_update(table,column1,value1,value2)

    elif command == "Удаление данных":
        table = input("Введите название таблицы: ")
        name = input("Введите наименование машины которую хотите удалить: ")
        db.delete_data(table, name)

    elif command == "\help": print("Список доступных команад: \n"
                                   "*Добавить данные\n"
                                   "*Показать данные в таблиц\n"
                                   "*Найти данные по значению в таблице\n"
                                   "*Изменение данных\n"
                                   "*Удаление данных\n")

    else: print("Данная команда не распознана, введите /help для вывода списка доступных команд")