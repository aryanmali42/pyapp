from tkinter import *
from PIL import ImageTk
from tkinter import messagebox,ttk
from subprocess import call        
import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.title("Main Detail Page")
root.geometry('1270x685')
id = StringVar()
name = StringVar()

transaction_details_frame=LabelFrame(root,text='Transaction Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame.pack(fill=X)
idLabel=Label(transaction_details_frame,text='Your Id',font=('times new roman',15,'bold'),fg='white',bg='grey20')
idLabel.grid(row=0,column=0,padx=20,pady=2)
idEntry=Entry(transaction_details_frame,font=('arial',15),bd=7,width=18,textvariable=id)#,textvariable=rollno)
idEntry.grid(row=0,column=1)

nameLabel=Label(transaction_details_frame,text='Your Name',font=('times new roman',15,'bold'),fg='white',bg='grey20')
nameLabel.grid(row=0,column=2,padx=20,pady=2)
nameEntry=Entry(transaction_details_frame,font=('arial',15),bd=7,width=18,textvariable=name)
nameEntry.grid(row=0,column=3)


typeLabel=Label(transaction_details_frame,text='Type',font=('times new roman',15,'bold'),fg='white',bg='grey20')
typeLabel.grid(row=0,column=4,padx=20,pady=2)
choices=['small','medium','large']
typeEntry=ttk.Combobox(transaction_details_frame,values=choices)
typeEntry.grid(row=0,column=5)


# def GET_DATA():
# 	con=pymysql.connect(host='localhost',user='root',password='',database='python_app')
# 	cur=con.cursor() 
# 	cur.execute('SELECT * FROM ')
# 	rows=cur.fetchall()
  			
# 	if len(rows)!=0: 
#          Student_table.delete(*Student_table.get_children())
#          for row in rows:
#              Student_table.insert('',END,values=row)
#          con.commit()
#          con.close()

getbtn=Button(transaction_details_frame,text='Sumbit',font=('Open Sans',10,'bold'),fg='white',bg='grey20',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=10)
getbtn.grid(row=0,column=6,padx=20,pady=2)
        #or dropdown ke leay
        #option=StringVar()
        #option.set('small')
        #typeEntry=OptionMenu(transaction_details_frame,option,'small','medium','large')
        #typeEntry.grid(row=0,column=5)

variableFrame=Frame(root)
variableFrame.pack()
#IP
transaction_details_frame1=LabelFrame(variableFrame,text='IP VAR',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame1.grid(row=0,column=0)
var1label=Label(transaction_details_frame1,text='VAR 1',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var1label.grid(row=0,column=0,pady=14,padx=10)
var2label=Label(transaction_details_frame1,text='VAR 2',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var2label.grid(row=1,column=0,pady=14,padx=10)
var3label=Label(transaction_details_frame1,text='VAR 3',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var3label.grid(row=2,column=0,pady=14,padx=10)
var4label=Label(transaction_details_frame1,text='VAR 4',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var4label.grid(row=3,column=0,pady=14,padx=10)
var5label=Label(transaction_details_frame1,text='VAR 5',font=('times new roman',15,'bold'),fg='white',bg='grey20')
var5label.grid(row=4,column=0,pady=14,padx=10)


#EV
var1ev=IntVar()
var2ev=IntVar()
var3ev=IntVar()
var4ev=IntVar()
var5ev=IntVar()
transaction_details_frame2=LabelFrame(variableFrame,text='EV Entry',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame2.grid(row=0,column=1)
var1Entry=Entry(transaction_details_frame2,textvariable=var1ev,font=('arial',15),bd=7,width=18)
var1Entry.grid(row=0,column=1,pady=9,padx=10)
var2Entry=Entry(transaction_details_frame2,textvariable=var2ev,font=('arial',15),bd=7,width=18)
var2Entry.grid(row=1,column=1,pady=9,padx=10)
var3Entry=Entry(transaction_details_frame2,textvariable=var3ev,font=('arial',15),bd=7,width=18)
var3Entry.grid(row=2,column=1,pady=9,padx=10)
var4Entry=Entry(transaction_details_frame2,textvariable=var4ev,font=('arial',15),bd=7,width=18)
var4Entry.grid(row=3,column=1,pady=9,padx=10)
var5Entry=Entry(transaction_details_frame2,textvariable=var5ev,font=('arial',15),bd=7,width=18)
var5Entry.grid(row=4,column=1,pady=9,padx=10)

#CV
var1cv=IntVar()
var2cv=IntVar()
var3cv=IntVar()
var4cv=IntVar()
var5cv=IntVar()
transaction_details_frame3=LabelFrame(variableFrame,text='CV Entry',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame3.grid(row=0,column=2)
cventry1=Entry(transaction_details_frame3,textvariable=var1cv,font=('arial',15),bd=7,width=18)
cventry1.grid(row=0,column=2,pady=9,padx=10)
cventry2=Entry(transaction_details_frame3,textvariable=var2cv,font=('arial',15),bd=7,width=18)
cventry2.grid(row=1,column=2,pady=9,padx=10)
cventry3=Entry(transaction_details_frame3,textvariable=var3cv,font=('arial',15),bd=7,width=18)
cventry3.grid(row=2,column=2,pady=9,padx=10)
cventry4=Entry(transaction_details_frame3,textvariable=var4cv,font=('arial',15),bd=7,width=18)
cventry4.grid(row=3,column=2,pady=9,padx=10)
cventry5=Entry(transaction_details_frame3,textvariable=var5cv,font=('arial',15),bd=7,width=18)
cventry5.grid(row=4,column=2,pady=9,padx=10)

#%C RESULT BLOCK
transaction_details_frame4=LabelFrame(variableFrame,text='%C RESULT',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame4.grid(row=0,column=3)


#D RANGE
dentryvar1=StringVar()
dentryvar2=StringVar()
dentryvar3=StringVar()
dentryvar4=StringVar()
dentryvar5=StringVar()

transaction_details_frame5=LabelFrame(variableFrame,text='D Range',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame5.grid(row=0,column=4)

dentry1 = ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", textvariable=dentryvar1)
dentry1["value"]=("Low","Medium","High")
dentry1.grid(row=0,column=1,pady=14,padx=10)

dentry2 = ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", textvariable=dentryvar2)
dentry2["value"]=("Low","Medium","High")
dentry2.grid(row=1,column=1,pady=14,padx=9)

dentry3=ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", textvariable=dentryvar3)
dentry3["value"]=("Low","NA","High")
dentry3.grid(row=2,column=1,pady=14,padx=9)

dentry4=ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", textvariable=dentryvar4)
dentry4["value"]=("Low","NA","High")
dentry4.grid(row=3,column=1,pady=14,padx=9)

dentry5=ttk.Combobox(transaction_details_frame5,font=('arial',15),state="readonly", textvariable=dentryvar5)
dentry5["value"]=("Low","NA","High")
dentry5.grid(row=4,column=1,pady=14,padx=9)



#ND RANGE
ndentryvar1=StringVar()
ndentryvar2=StringVar()
ndentryvar3=StringVar()
ndentryvar4=StringVar()
ndentryvar5=StringVar()
transaction_details_frame6=LabelFrame(variableFrame,text='ND_Range',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame6.grid(row=0,column=5)

ndentry1=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly",textvariable=ndentryvar1)
ndentry1["value"]=("Low","Medium","High")
ndentry1.grid(row=0,column=1,pady=14,padx=10)

ndentry2=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly",textvariable=ndentryvar2)
ndentry2["value"]=("Low","Medium","High")
ndentry2.grid(row=1,column=1,pady=14,padx=9)

ndentry3=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly",textvariable=ndentryvar3)
ndentry3["value"]=("Low","NA","High")
ndentry3.grid(row=2,column=1,pady=14,padx=9)

ndentry4=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly",textvariable=ndentryvar4)
ndentry4["value"]=("Low","NA","High")
ndentry4.grid(row=3,column=1,pady=14,padx=9)

ndentry5=ttk.Combobox(transaction_details_frame6,font=('arial',15),state="readonly",textvariable=ndentryvar5)
ndentry5["value"]=("Low","NA","High")
ndentry5.grid(row=4,column=1,pady=14,padx=9)



def calculate_c():
        evvar1=var1ev.get()
        evvar2=var2ev.get()
        evvar3=var3ev.get()
        evvar4=var4ev.get()
        evvar5=var5ev.get()
        cvvar1=var1cv.get()
        cvvar2=var2cv.get()
        cvvar3=var3cv.get()
        cvvar4=var4cv.get()
        cvvar5=var5cv.get()
        result1label=Label(transaction_details_frame4,text=(cvvar1/evvar1)*100,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        result1label.grid(row=0,column=3,pady=14,padx=10)
        result2label=Label(transaction_details_frame4,text=(cvvar2/evvar2)*100,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        result2label.grid(row=1,column=3,pady=14,padx=10)
        result3label=Label(transaction_details_frame4,text=(cvvar3/evvar3)*100,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        result3label.grid(row=2,column=3,pady=14,padx=10)
        result4label=Label(transaction_details_frame4,text=(cvvar4/evvar4)*100,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        result4label.grid(row=3,column=3,pady=14,padx=10)
        result5label=Label(transaction_details_frame4,text=(cvvar5/evvar5)*100,font=('times new roman',15,'bold'),fg='white',bg='grey20')
        result5label.grid(row=4,column=3,pady=14,padx=10)
        resvar1=(cvvar1/evvar1)*100
        resvar2=(cvvar2/evvar2)*100
        resvar3=(cvvar3/evvar3)*100
        resvar4=(cvvar4/evvar4)*100
        resvar5=(cvvar5/evvar5)*100

        if(resvar1<=50):
                dentryvar1.set('Low')
                ndentryvar1.set('NA')
        elif(resvar1>51 and resvar1<99):
                dentryvar1.set('Medium')
                ndentryvar1.set('NA')
        elif(resvar1>99):
                dentryvar1.set('NA')
                ndentryvar1.set('High')
        if(resvar2>=51 and resvar1<=100):
                dentryvar2.set('Medium')
                ndentryvar2.set('NA')
        elif(resvar2>99):
                dentryvar2.set('NA')
                ndentryvar2.set('High')
        elif(resvar2<=50):
                dentryvar2.set('NA')
                ndentryvar2.set('Low')
        if(resvar3<10):
                dentryvar3.set('Low')
                ndentryvar3.set('NA')
        elif(resvar3>10):
                dentryvar3.set('NA')
                ndentryvar3.set('High')
        if(resvar4<5):
                dentryvar4.set('Low')
                ndentryvar4.set('NA')
        elif(resvar4>5):
                dentryvar4.set('NA')
                ndentryvar4.set('High')
        if(resvar5>98):
                dentryvar5.set('High')
                ndentryvar5.set('NA')
        elif(resvar5<98):
                dentryvar5.set('NA')
                ndentryvar5.set('Low')




#BUTTON

variableFrame1=Frame(root)
variableFrame1.pack()
transaction_details_frame5=LabelFrame(variableFrame1,text="OPTIONS",font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='grey20')
transaction_details_frame5.grid(row=3,column=2)
calc_btn = Button(transaction_details_frame5,text = "Calculate %c",command=calculate_c,font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
calc_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)


total_btn = Button(transaction_details_frame5,text = "Show Result",font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
total_btn.grid(row = 1,column = 5,ipadx = 20,padx = 30)

        #========================
genbill_btn = Button(transaction_details_frame5,text = "Add",font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
genbill_btn.grid(row = 1,column = 6,ipadx = 20)

        #====================
clear_btn = Button(transaction_details_frame5,text = "Compare",font=("lucida",12,"bold"),bd = 7,relief = GROOVE)
clear_btn.grid(row = 1,column = 7,ipadx = 20,padx = 30)

        #======================
exit_btn = Button(transaction_details_frame5,text = "Exit",font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = exit)
exit_btn.grid(row = 1,column = 8,ipadx = 20)



#database System



#logic = SELECT username from login l join transaction t ON l.username=t.username WHERE l.username=

Frame_Data = Frame(root, bd=12, relief=GROOVE, bg="#e3f4f1")
Frame_Data.place(x=440 , y=450)
Frame_Database = Frame(Frame_Data, bd=11, relief=GROOVE)
Frame_Database.pack(fill=BOTH, expand=True)
Frame_Database.grid(row=3,column=2)
def GET_DATA():
	con=pymysql.connect(host='localhost',user='root',password='',database='python_app')
	cur=con.cursor() 
	cur.execute('SELECT * FROM transactions ')#cur.execute('SELECT * FROM transactions ')where etc
	rows=cur.fetchall()
	if len(rows)!=0: 
         for row in rows:
             Student_table.insert('',END,values=row)
         con.commit()
         con.close()

def FOCUS(e): 
	cursor=Student_table.focus()
	content=Student_table.item(cursor)
	row=content['values']
	name.set(row[0])
	id.set(row[1])
# Database Frame
Frame_Database = Frame(Frame_Data, bg="#e3f4f1", bd=1, relief=GROOVE)
Frame_Database.grid(row=3,column=2)
Scroll_X = Scrollbar(Frame_Database, orient=HORIZONTAL)
Scroll_Y = Scrollbar(Frame_Database, orient=VERTICAL)
Student_table = ttk.Treeview(Frame_Database, columns=("transaction_id", "transaction_name"), yscrollcommand= Scroll_Y.set,xscrollcommand= Scroll_X.set)
Scroll_X.config(command=Student_table.xview)
Scroll_X.pack(side=BOTTOM, fill=X)
Scroll_Y.config(command=Student_table.yview)
Scroll_Y.pack(side=RIGHT, fill=Y)
Student_table.heading("transaction_name", text="transaction_name")
Student_table.heading("transaction_id", text="transaction_id")
Student_table['show']='headings'
Student_table.column("transaction_name",width= 100)
Student_table.column("transaction_id",width= 100)
Student_table.pack(fill=BOTH, expand=True)
Student_table.pack(fill=BOTH, expand=True)
GET_DATA()
Student_table.bind("<ButtonRelease-1>",FOCUS)
root.mainloop()
