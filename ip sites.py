from tkinter import *
from socket import *
#####################################################
#this part for window
w = Tk()
w.title('Ip sites')
w.geometry('400x300+400+200')
w.resizable(0,0)
#####################################################
#this part for programming
Logo = PhotoImage(file='D:/naruto.gif')
var = StringVar()
var2 = StringVar()
def getip():
    var2.set(gethostbyname(var.get()))







#####################################################
#this part for design
#this part for Lables
LbImg = Label(w,
              image = Logo)

LbImg.place(x=0,y=0)

LbSite = Label(w,
               text = 'Website Here',
               bg='black',
               fg='red',
               font = ('arial',14,'bold'))
LbSite.place(x=20,y=70)

Lbget = Label(w,
              text = 'Ip : ',
               bg='black',
               fg='red',
               font = ('arial',14,'bold'))
Lbget.place(x=20,y=150)
######################################################
#this part for entries
entsite = Entry(w,bg='black',
               fg='red',
               font = ('arial',14,'bold'),
                bd = 6,
                textvariable = var)
entsite.place(x=150,y=70)

entget = Entry(w,bg='black',
               fg='red',
               font = ('arial',14,'bold'),
                bd = 6,
               textvariable = var2)
entget.place(x=70,y=150)
########################################################
#Buttons
bt = Button(w,bg='black',text='Get',
               fg='red',
               font = ('arial',14,'bold'),
                bd = 6,command = getip)
bt.place(x=320,y=140)


w.mainloop()
