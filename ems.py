from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database

def delete_all():
    result = messagebox.askyesno('Confirm','do you really want to delete all the record?')
    if result:
        database.deleteall_records()

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchbox.set('Search By')


def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','search box is empty')
    elif searchbox.get()=='Search By':
        messagebox.showerror('Error','please select the option')
    else:
        searched_data = database.search(searchbox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END,values = employee)


def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('success','successfully delete the data')



def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),rolebox.get(),Genderbox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','update successfully')


def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        rolebox.set(row[3])
        Genderbox.set(row[4])
        salaryEntry.insert(0,row[5])


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    salaryEntry.delete(0,END)
    rolebox.set('Web Developer')
    Genderbox.set('MALE')


def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values = employee)


def add_employee():
    if idEntry.get()==''or phoneEntry.get()==''or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required')

    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')

    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error','Invalid ID format. Use EMP before the number(e.g., EMP 1)')

    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),salaryEntry.get(),rolebox.get(),Genderbox.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is added')


window = CTk()
window.geometry('1200x600+50+50')
window.resizable(0,0)
window.title("Employee Management System")
window.configure(fg_color='black')


logo = CTkImage(Image.open('peakpx.jpg'),size=(1200,200))
logoLabel = CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan =2)


leftframe = CTkFrame(window,fg_color='black')
leftframe.grid(row=1,column = 0)


idLabel = CTkLabel(leftframe,text="ID",font=('arial',20,'bold'))
idLabel.grid(row= 0,column =0,padx= 20,pady = 15,sticky='w')


idEntry = CTkEntry(leftframe,font=('arial',20,'bold'),width=200)
idEntry.grid(row=0,column=1)


nameLabel = CTkLabel(leftframe,text="NAME",font=('arial',20,'bold'))
nameLabel.grid(row= 1,column =0,padx= 20,pady = 15, sticky='w')


nameEntry = CTkEntry(leftframe,font=('arial',20,'bold'),width=200)
nameEntry.grid(row=1,column=1)


phoneLabel = CTkLabel(leftframe,text="PHONE",font=('arial',20,'bold'))
phoneLabel.grid(row= 2,column =0,padx= 20,pady = 15, sticky='w')


phoneEntry = CTkEntry(leftframe,font=('arial',20,'bold'),width=200)
phoneEntry.grid(row=2,column=1)


roleLabel = CTkLabel(leftframe,text="ROLE",font=('arial',20,'bold'))
roleLabel.grid(row= 3,column =0,padx= 20,pady = 15, sticky='w')


roleoption = ['Web Developer','Cloud Architect','Technical Writter','Network Engineer','Data Scientist','business Analyst','IT consultant','UI Designer']
rolebox = CTkComboBox(leftframe,values=roleoption,width = 200,font=('arial',20,'bold'),state='readonly')
rolebox.grid(row = 3,column=1)
rolebox.set(roleoption[0])


GenderLabel = CTkLabel(leftframe,text="GENDER",font=('arial',20,'bold'))
GenderLabel.grid(row= 4,column =0,padx= 20,pady = 15, sticky='w')


Genderoption = ['MALE','FEMALE']
Genderbox = CTkComboBox(leftframe,values=Genderoption,width = 200,font=('arial',20,'bold'),state='readonly')
Genderbox.grid(row = 4,column=1)
Genderbox.set(Genderoption[0])


SalaryLabel = CTkLabel(leftframe,text="SALARY",font=('arial',20,'bold'))
SalaryLabel.grid(row= 5,column =0,padx= 20,pady = 15, sticky='w')


salaryEntry = CTkEntry(leftframe,font=('arial',20,'bold'),width=200)
salaryEntry.grid(row=5,column=1)


rightframe = CTkFrame(window)
rightframe.grid(row=1,column = 1)


searchoption = ['ID','PHONE','SALARY','GENDER','ROLE','NAME']
searchbox = CTkComboBox(rightframe,values=searchoption,width = 200,font=('arial',20,'bold'),state='readonly')
searchbox.grid(row = 0,column=0)
searchbox.set('Search By')


searchEntry = CTkEntry(rightframe,font=('arial',20,'bold'),width=200)
searchEntry.grid(row=0,column=1)


searchButton = CTkButton(rightframe,text='Search',width=100,command=search_employee)
searchButton.grid(row = 0, column = 2)


showButton = CTkButton(rightframe,text='Show All',width=100,command=show_all)
showButton.grid(row = 0, column = 3,pady = 5)


tree = ttk.Treeview(rightframe,height=13)
tree.grid(row = 1,column =0,columnspan=4)


tree['column']= ('ID','NAME','PHONE','ROLE','GENDER','SALARY')


tree.heading('ID',text= 'ID')
tree.heading('NAME',text= 'NAME')
tree.heading('PHONE',text= 'PHONE')
tree.heading('ROLE',text= 'ROLE')
tree.heading('GENDER',text= 'GENDER')
tree.heading('SALARY',text= 'SALARY')


tree.configure(show = 'headings')


tree.column('ID', width = 100)
tree.column('NAME', width = 160)
tree.column('PHONE', width = 160)
tree.column('ROLE', width = 180)
tree.column('GENDER', width = 100)
tree.column('SALARY', width = 130)

style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',15,'bold'))

style.configure('Treeview',font=('arial',12,'bold'),background= 'black',foreground = 'white')


scrollbar = ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)


buttonfram = CTkFrame(window,fg_color='black')
buttonfram.grid(row = 2,column=0,columnspan=2)


newButton = CTkButton(buttonfram,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0,column=0,pady=5)


addButton = CTkButton(buttonfram,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)


updateButton = CTkButton(buttonfram,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)


DeleteButton = CTkButton(buttonfram,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
DeleteButton.grid(row=0,column=3,pady=5,padx=5)


DeleteallButton = CTkButton(buttonfram,text='Delete all',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
DeleteallButton.grid(row=0,column=4,pady=5,padx=5)


treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()