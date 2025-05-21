import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor,conn
    try:
        conn = pymysql.connect(host = 'localhost',user = 'root', password= '12345')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error','something went wrong, please open mysql app beforetry again')
        return

    mycursor.execute('create database if not exists employee_data')
    mycursor.execute('use employee_data')
    mycursor.execute('create table if not exists data (id varchar(20), name varchar(50), phone varchar(15), role varchar(50), Gender varchar(10),salary decimal(10,2))')


def insert(id, name, phone, salary, role, Gender):
    query = 'INSERT INTO data (id, name, phone, role, Gender, salary) VALUES (%s, %s, %s, %s, %s, %s)'
    values = (id, name, phone, role, Gender, salary)
    mycursor.execute(query, values)
    conn.commit()

def id_exists(id):
    mycursor.execute('select count(*) from data where id = %s',id)
    result = mycursor.fetchone()
    return result[0]>0

def fetch_employees():
    mycursor.execute('select * from data')
    result = mycursor.fetchall()
    return result

def update(id, new_name, new_phone, new_role, new_gender, new_salary):
    mycursor.execute(
        'UPDATE data SET name=%s, phone=%s, role=%s, Gender=%s, salary=%s WHERE id=%s',
        (new_name, new_phone, new_role, new_gender, new_salary, id)
    )
    conn.commit()

def delete(id):
    mycursor.execute('delete from data where id=%s',id)
    conn.commit()


def search(option,value):
    mycursor.execute(f'select * from data where {option}=%s',value)
    result = mycursor.fetchall()
    return result

def deleteall_records():
    mycursor.execute('truncate table data')
    conn.commit()

connect_database()