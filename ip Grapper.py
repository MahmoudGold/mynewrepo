#this part for modules
from tkinter import *
from socket import *
#################################################################################
#this part for window
w = Tk()
w.title('Ip Grapper')
w.geometry('350x200+400+200')
w.resizable(0,0)
w.configure(bg='#000000')
#################################################################################
#this part for programming
var = StringVar()
def getip():
    from requests import get
    var.set(get('https://api.ipify.org').text)


#################################################################################
#this part for design
####################################
#this part for Button
btGet = Button(w,text='Get',
               bg = '#778899' ,
               fg = '#8B0000' ,
               bd = 6 , font = ('arial',14,'bold'),
               command = getip)
btGet.place(x = 150 , y = 100)
###################################
#this part for entry
ent = Entry(w,state='readonly',
            bd=6,
            bg='black',
            fg = '#8B0000',
            justify='center',
            font=('arial',16,'bold'),
            textvariable = var)
ent.place(x = 60 , y = 40)





w.mainloop()
