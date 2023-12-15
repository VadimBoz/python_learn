
from datetime import date
import csv
import os.path
import inspect

filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))

if os.path.isfile (f"{path}/notes.csv"):
    NOTES_FILE = f"{path}/notes.csv"
    print(f"\nФайл с заметками notes.cs  в каталоге\n {path} найден\n")
else:
    print(f"\nФайл с заметками notes.cs  в каталоге\n {path} не найден, создан новый\n")
    NOTES_FILE = f"{path}/notes.csv"
    with open(NOTES_FILE, mode='w', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")



def add_note():
    head_notes = input("Ведите название заметки > ")
    body_notes = input("Ведите тело заметки > ")
    current_date = date.today()
    count = 0
    with open(NOTES_FILE, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            count += 1

    with open(NOTES_FILE, mode='a', encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
        file_writer.writerow([count+1, current_date, head_notes, body_notes])
    
    print(f"Заметка '{head_notes}' успешно добавлена {current_date} \n\n\n")
    


def print_all_notes():
    print("")
    count = 0
    with open(NOTES_FILE, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            print(f"id: {row[0]}; Дата: {row[1]}; Заголовок: {row[2]};  Заметка: {row[3]}")
            count = count + 1
    if count == 0:
        out_red("     Заметок не найдено")
        out_wite("") 
    else:
        print(f"Найдено {count} заметок\n")        
            
            
            

def del_note_id():
    note_id = input("Ведите id заметки > ")
    notes = []
    count = 0
    with open(NOTES_FILE, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            if row[0] == note_id:
                count = count + 1
                out_red(f"     Заметка с id - {note_id} найдена")
                out_wite("")
            else:
                row[0] = int(row[0]) - count    
                notes.append(row)
        if count == 0:
            out_red(f"     Заметка с id - {note_id} не найдена")
            out_wite("")
        else:
            out_red(f"    Заметка с id - {note_id} удалена")
            out_wite("")  
    if count != 0:
        with open(NOTES_FILE, mode='w', encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
            for row in notes:
                file_writer.writerow(row)
            print('     Изменения сохранены\n\n')
        
def del_note_name():
    note_head = input("Ведите название заметки > ")
    notes = []
    count = 0
    flag = 0
    
    with open(NOTES_FILE, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            if row[2] == note_head:
                out_red(f"     Заметка с названием - {note_head} найдена")
                out_wite("")
                flag = 1
                print(f"id: {row[0]}; Дата: {row[1]}; Заголовок: {row[2]};  Заметка: {row[3]}")
                question  = input("\nВы хотите удалить данную заметку [y/n]? >")
                if question == "y":
                    count = count + 1
                    out_red(f"    Заметка с названием - {note_head} удалена")
                    out_wite("") 
                else: 
                    row[0] = int(row[0]) - count    
                    notes.append(row)  
            else:
                row[0] = int(row[0]) - count    
                notes.append(row)
        if flag == 0:
            out_red(f"     Заметка с названием - {note_head} не найдена")
            out_wite("")
    if count != 0:
        with open(NOTES_FILE, mode='w', encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
            for row in notes:
                file_writer.writerow(row)
            print('     Изменения сохранены\n\n')
    


def edit_note_id():
    note_id = input("Ведите id заметки > ")
    notes = []
    count = 0
    with open(NOTES_FILE, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            if row[0] == note_id:
                count = count + 1
                out_red(f"     Заметка с id - {note_id} найдена")
                out_wite("")
                print(f"id: {row[0]}; Дата: {row[1]}; Заголовок: {row[2]};  Заметка: {row[3]}")
                question  = input("\nВы хотите изменить данную заметку [y/n]? >")
                if question == "y":
                    note_head = input("Ведите название заметки > ")
                    body_notes = input("Ведите тело заметки > ")
                    current_date = date.today()
                    row[1] = current_date
                    row[2] = note_head
                    row[3] = body_notes
                    notes.append(row)
                    out_red(f"    Заметка с названием - {note_head} изменена")
                    out_wite("") 
            else:    
                notes.append(row)
        if count == 0:
            out_red(f"     Заметка с id - {note_id} не найдена")
            out_wite("")  
    if count != 0:
        with open(NOTES_FILE, mode='w', encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
            for row in notes:
                file_writer.writerow(row)
            print('     Изменения сохранены\n\n')



def edit_note_name():
    note_head = input("Ведите название заметки > ")
    notes = []
    count = 0
    with open(NOTES_FILE, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            if row[2] == note_head:
                count = count + 1
                out_red(f"     Заметка с названием - {note_head} найдена")
                out_wite("")
                print(f"id: {row[0]}; Дата: {row[1]}; Заголовок: {row[2]};  Заметка: {row[3]}")
                question  = input("\nВы хотите изменить данную заметку [y/n]? >")
                if question == "y":
                    note_head2 = input("Ведите название заметки > ")
                    body_notes2 = input("Ведите тело заметки > ")
                    current_date2 = date.today()
                    row[1] = current_date2
                    row[2] = note_head2
                    row[3] = body_notes2
                    notes.append(row)
                    print("")
                    out_red(f"    Заметка с названием - {note_head2} изменена")
                    out_wite("") 
                else: 
                    print("")
                    out_red(f"    Заметка с названием - {note_head} не была изменена")
                    out_wite("") 
                    notes.append(row)    
            else:    
                notes.append(row)
                
        if count == 0:
            out_red(f"     Заметка с названием - {note_head} не найдена")
            out_wite("")  
    if count != 0:
        with open(NOTES_FILE, mode='w', encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
            for row in notes:
                file_writer.writerow(row)
            print('     Изменения сохранены\n\n')
    
    


def print_note_for_date():
    note_date = input("Введите дату заметок в формате yyyy-mm-dd > ")
    print("")
    count = 0
    with open(NOTES_FILE, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")
        for row in file_reader:
            if row[1] == note_date:
                count = count + 1
                print(f"id: {row[0]}; Дата: {row[1]}; Заголовок: {row[2]};  Заметка: {row[3]}")
        if count == 0:
            out_red(f"     Заметок за дату  - {note_date} не найдено")
            out_wite("") 
        else:
             print(f"Найдено {count} заметок")

def out_red(text):
    print("\033[31m {}" .format(text))
def out_wite(text):
    print("\033[37m {}" .format(text))


while (True):
    print("\n--------------------Программа для работы с заметками----------------------\n")
    print("Введите номер пункта  меню:\n")
    print("1 -  Добавить новую заметку")
    print("2 -  Список всех заметок")
    print("3 -  Удалить заметку по id")
    print("4 -  Удалить заметку по названию")
    print("5  - Редактировать заметку по id")
    print("6  - Редактировать заметку по по названию")
    print("7  - Вывести список заметок за определенную дату")
    print("8 -  Завершить работу с программой")
    number_menu = input("\nВведите номер меню: > ")
    
    match number_menu:
        case "1":
            add_note()
        case "2":
            print_all_notes()
        case "3":
            del_note_id()
        case "4":
            del_note_name()
        case "5":
            edit_note_id()
        case "6":
            edit_note_name()
        case "7":
            print_note_for_date()
        case "8":
            print('\nРабота с программой завершена!\n')
            break       
        case _:
            out_red("\n Вы ввели неверный номер меню, попробуйте снова\n\n")
            out_wite("")