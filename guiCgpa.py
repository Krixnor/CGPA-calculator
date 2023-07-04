from tkinter import *
import sqlite3
import pandas as pd
from datetime import date as dt
from PIL import Image
from PIL import ImageTk
import customtkinter
from tkinter.messagebox import showerror, showinfo

win = customtkinter.CTk()
win.title('cgpa Calculator')
win.geometry('400x500')
win.resizable(0,0)
win.iconbitmap(r"C:\Users\user\Documents\CGPA1\download.ico")
#win['fg'] = 'blue'
colour = '#1b2328'
col = StringVar()
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode('dark')

font_header = ("Helvetica", 20, "bold")
font_btn = ("sans-serif", 20, "bold")
count = 0
cc = 0

def intcheck(entry):
        try:
            int(entry)
            return True
        except:
            return False
    

def check():
    global p,point,t2,t4
    p=0
    e2 = l2.get()
    t2 = e2.upper()
    e4 = l4.get()
    t4 = e4.title()
    if t2 == '':
       showerror(title='info',message='please enter valid course code')
    elif l3.get() == '':
        showerror(title='info',message='please entergrade point')
    elif intcheck(l3.get()) is False:
        showerror(title='info',message='Grade point must be a number')
    elif t4 == '':
        showerror(title='info',message='please enter Grade')
    elif t4 == 'A':
        g= p+5
        p=g
        point = p * int(l3.get())
        so()
        #print(p)
    elif t4 == 'B':
        g = p+4
        p=g
        point = p * int(l3.get())
        so()
    elif t4 == 'C':
        g=p+3
        p=g
        point = p * int(l3.get())
        so()
    elif t4 == 'D':
        g=p+2
        p=g
        point = p * int(l3.get())
        so()
    elif t4 == 'E':
        g=p+1
        p=g
        point = p * int(l3.get())
        so()
    elif t4 == 'F':
        g=0
        p=g
        point = p * int(l3.get())
        so()
    else:
        showerror(title='info',message='Invalid input')


def so():
    global cc,fcc
    cn = sqlite3.connect('rec.db')
    cur = cn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS record(
            courseCode varchar(6),
            creditLoad integer,
            Grade varchar(1),
            GradePoint integer,
            totalPoint integer
            )""")

    cur.execute("INSERT INTO record(courseCode,creditLoad,Grade,GradePoint,totalPoint) VALUES(?,?,?,?,?)",(t2,l3.get(),t4,p,point))
    cn.commit()
    
    cc+=1
    fcc = str(cc), 'added'
    col.set(fcc)
    clear()
    
    
    print('yoto')
    print(p)
    print(point)
    print(cc)

def cal():
    try:
        global final
        cn = sqlite3.connect('rec.db')
        cur = cn.cursor()
        df = pd.read_sql_query('SELECT * FROM record',con=sqlite3.connect('rec.db'))
        #print(df)
        data = df.sum()
        print(data)
        ans= data['totalPoint']/data['creditLoad']
        final = 'Your CGPA is '+ str(round(ans,1))
        col.set(final)
        cn.commit()
        drop()
    except:
        col.set('')
        pass

def drop():
    cn = sqlite3.connect('rec.db')
    cur = cn.cursor()
    cur.execute("DROP TABLE record")
    cn.commit()
       
def clear():
        l2.delete(0,END)
        l3.delete(0,END)
        l4.delete(0,END)
        
    
def h1():
    global l2,l3,l4,inputField
    #l1 = customtkinter.CTkLabel(master=win,text='Fill in the fields',text_color='white',font=font_header,
    #fg_color='teal')
    #l1.place(x=120,y=10)
    inputFrame = customtkinter.CTkFrame(master=win,width=300,corner_radius=10,height=100)
    inputFrame.pack(side=TOP,pady=20)
    inputField = customtkinter.CTkEntry(master=inputFrame,width=300,height=100 ,font=font_btn,justify=CENTER,textvariable=col,
    border_width=0, text_color='white').pack()

    l2 = customtkinter.CTkEntry(master=win,placeholder_text='Course Code',placeholder_text_color='grey',fg_color='white',border_color='blue',
    text_color='black',font=font_header,border_width=1,width=300,corner_radius=10)
    l2.place(x=50,y=200)

    l3 = customtkinter.CTkEntry(master=win,placeholder_text='Course Unit',placeholder_text_color='grey',fg_color='white',
    text_color='black',border_color='blue',border_width=1, font=font_header,width=300,corner_radius=10)
    l3.place(x=50,y=250)

    l4 = customtkinter.CTkEntry(master=win,placeholder_text='Grade(A-F)',placeholder_text_color='grey',fg_color='white',border_color='blue',
    border_width=1, text_color='black',font=font_header,width=300,corner_radius=10)
    l4.place(x=50,y=300)

    b1 = customtkinter.CTkButton(master=win,text='+Add',width=10,text_color='white',command=check)
    b1.place(x=180,y=400)

    b2 = customtkinter.CTkButton(master=win,text='Calculate CGPA',width=10,text_color='white',command=cal)
    b2.place(x=150,y=450)


    


#phone = customtkinter.CTkEntry(master=frame8,width=300,placeholder_text='Edit Phone no',placeholder_text_color='grey',font=ph,
#border_color=border,fg_color='black',text_color='white',corner_radius=10)
#phone.place(x=10,y=220)



    win.mainloop()
h1()
