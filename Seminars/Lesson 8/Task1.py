"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""
from csv import DictReader, DictWriter
from os.path import exists

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            second_name = input('Фамилия: ')
            if len(second_name) < 4:
                raise NameError("Слишком короткая фамилия")
            phone_number= input("Телефон: ")
            if len(phone_number) < 11:
                raise NameError("Слишком короткий телефон")
        except NameError as err:
            print(err)
        else:
            flag = True   
            
    return [first_name, second_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding ='UTF-8', newline='') as file:
        f_w = DictWriter(file, fieldnames= ['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()

def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    standard_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding ='UTF-8') as data:
        f_r = DictReader(data)
        return list(f_r)  #ящик со словарями
    
def remove_row(file_name):
    search = int(input("Введите номер строки для удаления: "))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search-1)
        standard_write(file_name, res)
    else:
        print("Введен неверный номер")

def standard_write(file_name, res):
    with open(file_name, 'w', encoding ='UTF-8', newline='') as file:
        f_w = DictWriter(file, fieldnames= ['first_name', 'second_name', 'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)

def copy_data(file_name_from, file_name_to):
    search = int(input("Введите номер строки для копирования: "))
    res = read_file(file_name_from)
    lst = read_file(file_name_to)
    if search <= len(res):
        lst.append(res[search-1])
        standard_write(file_name_to, lst)
    else:
        print("Введен неверный номер")

file_name_s = 'fromphone.csv'
file_name_t = 'tophone.csv'


def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name_s):
                create_file(file_name_s)
            write_file(file_name_s)
        elif command == 'rs':
            if not exists(file_name_s):
                print("Файла нет, создайте его")
                continue
            print(*read_file(file_name_s))
        elif command == 'rt':
            if not exists(file_name_t):
                print("Файла нет, создайте его")
                continue
            print(*read_file(file_name_t))    
        elif command == 'ds':
            if not exists(file_name_s):
                print("Файла нет, создайте его")
            remove_row(file_name_s)
        elif command == 'dt':
            if not exists(file_name_t):
                print("Файла нет, создайте его")
            remove_row(file_name_t)
        elif command == 'c':
            if not exists(file_name_s):
                print("Нет файла, откуда копировать данные, создайте его")
                create_file(file_name_s)
            if not exists(file_name_t):
                print("Нет файла, куда копировать, создайте его")
                create_file(file_name_t)
            copy_data(file_name_s, file_name_t)
            print(*read_file(file_name_t))
            



main()

