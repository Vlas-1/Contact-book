import sys
import sqlite3
import argparse
contact_name='' #Имя контакта
contact_num='' #Номер контакта
conn = sqlite3.connect('orderese.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
   name TEXT,
   number TEXT);
""")
conn.commit()

def add_contact(contact_num,contact_name): #Добавление контакта
    contact_name=input("Введите имя контакта:")
    contact_num=input("Ведите номер контакта:")
    cur.execute('INSERT INTO contacts(name, number) VALUES(?,?)', (contact_name, contact_num))
    conn.commit()
    remove1()
def delete_contact(): #Удаление контакта
    del_contact=input("Имя контакта которого нужно удалить:")
    cur.execute('DELETE FROM contacts WHERE name=?', [del_contact])
    conn.commit()
    remove1()
def cloud_save(): #Просмотр сохраннёного контакта
    cur.execute("SELECT * FROM contacts;")
    one_result = cur.fetchone()
    print(one_result)
    remove1()
def remove(): #Начальный ввод
    can=int(input("Что делать? Добавить контакт-0, Удалить контакт-1, Показать все контакты-2:"))
    if can==0:
        add_contact(contact_num,contact_name)
    if can==1:
        delete_contact()
    if can==2:
        cloud_save()
def remove1(): #Постоянный ввод
    can1=int(input("Введите цифру:"))
    if can1==0:
        add_contact(contact_num,contact_name)
    if can1==1:
        delete_contact()
    if can1==2:
        cloud_save()
def parsing(): #Парсинг
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', action='store_true', help='add contact')
    parser.add_argument('-d', '--delete', action='store_true', help='delete contact')
    parser.add_argument('-c', '--cloud', action='store_true', help='all contacts')
    args = parser.parse_args()
    parser.print_help()    
parsing()
remove()
