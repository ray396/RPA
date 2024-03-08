from tkinter import *

tela = Tk()
tela.title("Interface Gráfica")
rotulo1 = Label(tela, text="FLAT", relief=FLAT)
rotulo2 = Label(tela, text="RAISED", relief=RAISED)
rotulo3 = Label(tela, text="SUNKEN", relief=SUNKEN)
rotulo4 = Label(tela, text="GROOVE", relief=GROOVE)
rotulo5 = Label(tela, text="RIDGE", relief=RIDGE)

rotulo1.pack()
rotulo2.pack()
rotulo3.pack()
rotulo4.pack()
rotulo5.pack()

tela.mainloop()

tela = Tk()
tela.title("Interface Gráfica")
rotulo1 = Label(tela, text="Python", relief=FLAT, bg="green", fg="white")
rotulo2 = Label(tela, text="Python", relief=FLAT, bg="blue", fg="white", font="Times 24")

rotulo1.pack()
rotulo2.pack()