from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,ttk
#import pymysql
#import pymysql as mq
import mysql.connector
def login_page():
    signup_window.destroy()
    import login.py
def connect_database():
    if usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry=='':
        messagebox.showerror('Error','All Feilds Are Required')
    elif passwordEntry.get() != confirmEntry.get():
         messagebox.showerror('Error','Password MisMatch')
    elif check.get()==0:
        messagebox.showerror('Error','Please Except Terms and condition')
    else:
        try:
            con=mysql.connector.connect(host='localhost',user='root',password='',database="python_app")
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection Has Not Established Try Again')
            return
    query ='use python_app'
    mycursor.execute(query)

    query='insert into login(username,password) values(%s,%s)'
    mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
    con.commit()
    con.close()
    messagebox.showerror('sucess','Login Sucessfull')
    signup_window.destroy()
    import login.py
#GUI PART
signup_window=Tk()
#   signup
#_window.geometry('1968x980+50+50')
#signup_window.resizable(0,0)
signup_window.title('Signup Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=bgImage)
bgLabel.pack()
frame=Frame(signup_window,bg='white')
frame.place(x=454,y=80)

heading=Label(frame,text='Create An Account',font=('Microsoft Yahei UI Light',23,'bold'),fg='firebrick1',bg='white'
              )
heading.grid(row=0,column=0)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(20,0))

usernameEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
usernameEntry.grid(row=2,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
passwordEntry.grid(row=4,column=0,sticky='w',padx=25)

confirmLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',15,'bold'),bg='white',fg='firebrick1')
confirmLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry=Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
confirmEntry.grid(row=6,column=0,sticky='w',padx=25)
check=IntVar()
termsandconditions=Checkbutton(frame,text='I agree to Terms & Conditions',
                                font=('Microsoft Yahei UI Light',10,'bold'),
                               fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2',variable=check)
termsandconditions.grid(row=7,column=0,pady=5,padx=15)

signupButton=Button(frame,text='SignUp',font=('Open Sans',16,'bold'),bd=0,bg='firebrick',fg='white',activebackground='firebrick1',activeforeground='white',width=17,cursor='hand2',command=connect_database)
signupButton.grid(row=9,column=0,padx=15,pady=10)

loginButton=Button(frame,text='Already Have An Account LoginIn',font=('Open Sans',9,'bold'),
                   bd=0,
                   bg='white',fg='blue',activebackground='white',
                   activeforeground='blue',cursor='hand2',command=login_page)
loginButton.grid(row=11,column=0,padx=15,pady=10)
#loginButton.grid(row=11,padx=122,pady=10)

signup_window.mainloop()