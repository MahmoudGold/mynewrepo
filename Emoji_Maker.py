from tkinter import *
import tkinter as tk
from tkinter import ttk
##############################
#this part for window
w = Tk()
w.title('Emoji Maker V.1')
w.geometry('800x600+300+75')
w.configure(bg='#FFD700')
##############################
#this part for programming
color = "#FFD700"
style = ttk.Style()



##########################
#this part for designing...
#this part for images






####
#this part for Lables
Lb = Label(w,text = 'Emoji Maker',
           font=('arial',20,'bold'),
           bg='#FFD700',
           bd=10,
           relief='raised')

Lb.place(x=300,y=3)
###########################
#this part for LablesFrame
#Control Frame
fmC = LabelFrame(w,bg='#FFD700',width=400,height=400)
fmC.place(x=200,y=200)

###########################
#NoteBookes
ntb= ttk.Notebook(w)
#Frames
fmEyes = LabelFrame(ntb,bg='#FFD700')
fmMouse = LabelFrame(ntb,bg='#FFD700')
fmCharacteristics = LabelFrame(ntb,bg='#FFD700')

ntb.add(fmEyes , text = 'Eyes')
ntb.add(fmMouse , text = 'Mouses')
ntb.add(fmCharacteristics, text = 'Characteristics')



ntb.place(x=20,y=200)
############################
#fmEyes
bt1 = Button(fmEyes,text = 'Eye1',bg='#FFD700',activebackground='#FFD700')
bt1.pack()
bt2 = Button(fmEyes,text = 'Eye2',bg='#FFD700',activebackground='#FFD700')
bt2.pack()
bt3 = Button(fmEyes,text = 'Eye3',bg='#FFD700',activebackground='#FFD700')
bt3.pack()
bt4 = Button(fmEyes,text = 'Eye4',bg='#FFD700',activebackground='#FFD700')
bt4.pack()
bt5 = Button(fmEyes,text = 'Eye5',bg='#FFD700',activebackground='#FFD700')
bt5.pack()
bt6 = Button(fmEyes,text = 'Eye6',bg='#FFD700',activebackground='#FFD700')
bt6.pack()
bt7 = Button(fmEyes,text = 'Eye7',bg='#FFD700',activebackground='#FFD700')
bt7.pack()
bt8 = Button(fmEyes,text = 'Eye8',bg='#FFD700',activebackground='#FFD700')
bt8.pack()
bt9 = Button(fmEyes,text = 'Eye9',bg='#FFD700',activebackground='#FFD700')
bt9.pack()

bt10 = Button(fmEyes,text = 'Glasses 1',bg='#FFD700',activebackground='#FFD700')
bt10.pack()
bt11 = Button(fmEyes,text = 'Glasses 2',bg='#FFD700',activebackground='#FFD700')
bt11.pack()
bt12 = Button(fmEyes,text = 'Glasses 3',bg='#FFD700',activebackground='#FFD700')
bt12.pack()
bt13 = Button(fmEyes,text = 'Glasses 4',bg='#FFD700',activebackground='#FFD700')
bt13.pack()
######################################
#fmMouse
bt14 = Button(fmMouse,text = 'Mouth1',bg='#FFD700',activebackground='#FFD700')
bt14.pack()
bt15 = Button(fmMouse,text = 'Mouth2',bg='#FFD700',activebackground='#FFD700')
bt15.pack()
bt16 = Button(fmMouse,text = 'Mouth3',bg='#FFD700',activebackground='#FFD700')
bt16.pack()
bt17 = Button(fmMouse,text = 'Mouth4',bg='#FFD700',activebackground='#FFD700')
bt17.pack()
bt18 = Button(fmMouse,text = 'Mouse5',bg='#FFD700',activebackground='#FFD700')
bt18.pack()
######################################
#fmCharacteristics
bt19 = Button(fmCharacteristics,text = 'Crown',bg='#FFD700',activebackground='#FFD700')
bt19.pack()
bt20 = Button(fmCharacteristics,text = 'hat1',bg='#FFD700',activebackground='#FFD700')
bt20.pack()
bt21 = Button(fmCharacteristics,text = 'hat2',bg='#FFD700',activebackground='#FFD700')
bt21.pack()
bt22 = Button(fmCharacteristics,text = 'cap',bg='#FFD700',activebackground='#FFD700')
bt22.pack()
bt23 = Button(fmCharacteristics,text = 'cap2',bg='#FFD700',activebackground='#FFD700')
bt23.pack()
######################################
######theme
style.theme_create( "yummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": color },
            "map":       {"background": [("selected", color)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("yummy")

w.mainloop()
