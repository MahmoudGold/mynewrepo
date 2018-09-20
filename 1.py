########################################
#this part for window
from tkinter import *
w = Tk()
w.geometry('500x100+400+200')
w.title('Login')
w.configure(bg = '#000000')
w.resizable(0,0)
############################################
#this part for programming
############################################
var = StringVar()
mail = StringVar()
Pass = StringVar()
def do():
    if mail.get() == 'Kaneki' and Pass.get() == '123':
        var.set('Welcome In Your Account ! ')

    else :
        var.set('Invalid email or password . ')

########################################
#this part for design :
#this part for Lables
lbinfo = Label(w,
               bg = '#000000'
               ,fg='gold',
               font = ('arial',10,'bold'),
               textvariable = var
               )
lbinfo.place(x = 200 , y = 60)




########################################
lbemail = Label(w,
              text = 'E-mail',
              font = ('arial',10,'bold'),
              fg='gold',
              bg='#000000')
lbemail.place(x = '50' , y = '20')
########################################
lbPassword = Label(w,
              text = 'Password',
              font = ('arial',10,'bold'),
              fg='gold',
              bg='#000000')

lbPassword.place(x = '300' , y = '20')
#########################################
#this part for entry
entmail = Entry(w,
                bg = '#000000',
                fg= '#DAA520',
                textvariable = mail)
entmail.place(x = 100 , y = 20)
########################################
entpassword = Entry(w,bg = '#000000',
                fg= '#DAA520',
                textvariable = Pass,
                    show = '*')

entpassword.place(x = 370 , y = 20)
########################################

#this part for Buttons
btLogin = Button(w,text = 'Login' , font = ('arial',10,'bold'),
              fg='gold',
              bg='#000000',
                 command = do)
btLogin.place(x = 440 , y = 50)
w.mainloop()
