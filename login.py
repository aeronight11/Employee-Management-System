from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntery.get()==''or userpasswordEntery.get()=='':
        messagebox.showerror('Error','all fields are required')
    elif usernameEntery.get()=='krishna' and userpasswordEntery.get()=='1234':
        messagebox.showinfo('success',"login is successfully")
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','password or username is wrong')

def signup():
    root.destroy()
    import signup


root = CTk()
root.geometry('1000x600+50+50')
root.resizable(0,0)
root.title("login page")

image = CTkImage(Image.open("SL-093020-35920-01.jpg"), size =(1000, 600) )
imageLabel = CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)

headinglable = CTkLabel(root,text = "Employee Management System",bg_color="#000d2d", font=('Times New Roman',25,'bold'),text_color="gold")
headinglable.place(x= 30, y = 150)

usernameEntery = CTkEntry(root,placeholder_text= 'Enter Your Username',width=200)
usernameEntery.place(x=65, y= 220)

userpasswordEntery = CTkEntry(root,placeholder_text= 'Enter Your Password',width=200,show= '*')
userpasswordEntery.place(x= 65,y=270)

loginButton = CTkButton(root,text='Login',cursor = 'hand2',command=login)
loginButton.place(x=90,y=330)

signupButton = CTkButton(root,text='Sign up',cursor = 'hand2',command=signup)
signupButton.place(x=90,y=380)


root.mainloop()