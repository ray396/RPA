from tkinter import *

tela = Tk()
tela.title("Interface Gráfica")
rotulo1 = Label(tela, text="Python", relief=FLAT, bg="green", fg="white")
rotulo2 = Label(tela, text="Python", relief=FLAT, bg="blue", fg="white", font="Times 24")

rotulo1.pack()
rotulo2.pack()


tela.mainloop()