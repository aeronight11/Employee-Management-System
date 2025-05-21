from customtkinter import *
from PIL import Image
from tkinter import messagebox

def verify_id():
    import verify_id

create = CTk()
create.geometry('1000x600+50+50')
create.resizable(0,0)
create.title("signup page")

image = CTkImage(Image.open("SL-093020-35920-01.jpg"), size =(1000, 600) )
imageLabel = CTkLabel(create,image=image,text='')
imageLabel.place(x=0,y=0)

headinglable = CTkLabel(create,text = "Employee Management System",bg_color="#000d2d", font=('Times New Roman',25,'bold'),text_color="gold")
headinglable.place(x= 30, y = 150)

usernameEntery = CTkEntry(create,placeholder_text= 'create Your Username',width=200)
usernameEntery.place(x=65, y= 220)

userpasswordEntery = CTkEntry(create,placeholder_text= 'create Your Password',width=200,show= '*')
userpasswordEntery.place(x= 65,y=270)

userphoneEntery = CTkEntry(create,placeholder_text= 'Enter Your Phone no.',width=200,show= '*')
userphoneEntery.place(x= 65,y=320)

verifyButton = CTkButton(create,text='verify',cursor = 'hand2',command=verify_id)
verifyButton.place(x=90,y=370)



create.mainloop()