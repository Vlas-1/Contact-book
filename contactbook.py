import sys
import sqlite3
import argparse
contact_name=''
contact_num=''
Contacts=['Ваши контакты:']
colContacts=0
del_contact=0
conn = sqlite3.connect('orderese.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
   name TEXT,
   number TEXT);
""")
conn.commit()

def add_contact(contact_num,contact_name,Contacts,colContacts): #Добавление контакта
    contact_name=input("Введите имя контакта:")
    contact_num=input("Ведите номер контакта:")
    cur.execute('INSERT INTO contacts(name, number) VALUES(?,?)', (contact_name, contact_num))
    conn.commit()
    remove1(del_contact)
def delete_contact(del_contact,Contacts): #Удаление контакта
    del_contact=input("Имя контакта которого нужно удалить. Для отмены введите-5:")
    cur.execute('DELETE FROM contacts WHERE name=?', [del_contact])
    conn.commit()
    remove1(del_contact)
def cloud_save(): #Просмотр сохраннёного контакта
    cur.execute("SELECT * FROM contacts;")
    one_result = cur.fetchone()
    print(one_result)
    remove1(del_contact)
def remove(): #Начальный ввод
    can=int(input("Что делать? Добавить контакт-0, Удалить контакт-1, Показать сохранёный контакт-2, Выход-3:"))
    if can==0:
        add_contact(contact_num,contact_name,Contacts,colContacts)
    if can==1:
        delete_contact(del_contact,Contacts)
    if can==2:
        cloud_save()
    if can==3:
        sys.exit()
def remove1(del_contact): #Постоянный ввод
    can1=int(input("Что делать? Добавить контакт-0, Удалить контакт-1, Показать сохранёный контакт-2, Выход-3:"))
    if can1==0:
        add_contact(contact_num,contact_name,Contacts,colContacts)
    if can1==1:
        delete_contact(del_contact,Contacts)
    if can1==2:
        cloud_save()
    if can1==3:
        sys.exit()
def parsing(): #Парсинг
    parser = argparse.ArgumentParser()
    parser.add_argument('-0', '--add', action='store_true', help='add contact')
    parser.add_argument('-1', '--delete', action='store_true', help='delete contact')
    parser.add_argument('-2', '--cloud', action='store_true', help='save contact')
    parser.add_argument('-3', '--exit', action='store_true', help='exit')
    args = parser.parse_args()
    parser.print_help()
    if args.add:
        add_contact()
    if args.delete:
        delete_contact()
    if args.cloud:
        cloud_save()
parsing()
remove()

