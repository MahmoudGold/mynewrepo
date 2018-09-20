from tkinter import *
####################################
#this part for window
#######################################
w = Tk()
w.title('Simple Calculator')
w.geometry('300x300+400+200')
w.configure(bg='black')
w.configure(bd=6,relief='raised')
w.resizable(0,0)
########################################
#this part for programming Simple Calculator
total = StringVar()
frist = StringVar()
second = StringVar()

def add_plus():
    total.set('+')
def add_min():
    total.set('-')
def add_mult():
    total.set('x')
def add_div():
    total.set('/')
def sum_():
    try:
        if total.get()=='+':
            total.set(int(frist.get())+int(second.get()))
            frist.set('')
            second.set('')
        elif total.get()=='-':
            total.set(int(frist.get())-int(second.get()))
            frist.set('')
            second.set('')
        elif total.get()=='x':
            total.set(int(frist.get())*int(second.get()))
            frist.set('')
            second.set('')
        elif total.set()=='/':
            total.set(int(frist.get())//int(second.get()))
            frist.set('')
            second.set('')
    except Exception:
            pass
            total.set('Enter an Integer.')
            
########################################
#this part for design Simple Calculator
#############################
#this part for Lables (Simple Calculator)
lb1 = Label(w,
            text = 'Frist Number',
            bg = 'black',
            fg='red')
lb1.place(x=20,y=20)

lb2 = Label(w,
            text = 'Second Number',
            bg='black',
            fg='red')
lb2.place(x=15,y=70)

lbT = Label(w,
            text = 'Total',
            bg='black',
            fg='red')
lbT.place(x=20,y=220)
############################
#this part for Entries (Simple Calculator)
ent1 = Entry(w,
             bg='red',
             fg='black',
             bd=6,
             font = ('arial',10,'bold'),
             textvariable = frist)

ent1.place(x=100,y=20)

ent2 = Entry(w,
             bg='red',
             fg='black',
             bd=6,
             font = ('arial',10,'bold'),
             textvariable = second)
ent2.place(x=100,y=70)

entT = Entry(w,
             bg='red',
             fg='black',
             bd=6,
             font = ('arial',13,'bold'),
             textvariable = total)
entT.place(x=80,y=220)
###############################
#this part for Buttons (Simple Calculator)
btsum = Button(w,
               text = 'Sum',bg='red',
             fg='black',
             bd=6,
             font = ('arial',10,'bold'),
               activebackground = 'red',
               command = sum_)
btsum.place(x=130,y=260)
#############################################
btplus = Button(w,
               text = '+',bg='red',
             fg='black',
             bd=6,
             font = ('arial',10,'bold'),
               activebackground = 'red',
                command = add_plus)
btplus.place(x=170,y=150)
#############################################
btmin = Button(w,
               text = '-',bg='red',
             fg='black',
             bd=6,
             font = ('arial',10,'bold'),
               activebackground = 'red',
               command = add_min)
btmin.place(x=150,y=150)
#############################################
btmult = Button(w,
               text = 'x',bg='red',
             fg='black',
             bd=6,
             font = ('arial',10,'bold'),
               activebackground = 'red',
                command = add_mult)
btmult.place(x=103,y=150)
##############################################
btdiv = Button(w,
               text = '/',bg='red',
             fg='black',
             bd=6,
             font = ('arial',10,'bold'),
               activebackground = 'red',
               command = add_div)
btdiv.place(x=130,y=150)
###############################################
w.mainloop()
