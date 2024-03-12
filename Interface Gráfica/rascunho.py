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

texto = """ Curso de Tkinter
Aprendendo como criar
Interface gráfica com 
Python
"""
formato = Label(tela,
                font = "Arial 40 bold",
                text = texto).pack()

tela.mainloop()


tela.title("Tela 3 x 3")

for linha in range(5):
    for coluna in range(3):
        tabela = Frame(
            master= tela,
            relief= RAISED,
            borderwidth= 1
        )
        tabela.grid(row=linha, column= coluna, padx=5, pady=5)
        label = Label(master=tabela, text=f"Linha {linha}\n Coluna {coluna}")
        label.pack()

tela.mainloop()

janela = Tk()

janela.title("Botões")

def exibirMensagem():
    print("Ola Mundo!")

botao = Button(janela, text= "Clique aqui", command= exibirMensagem)
botao.pack()

janela.mainloop()

janela = Tk()
janela.title("Botões")

def exibirMensagem():
    print("Curso de Tkinter!")

entrar = Button(janela, text= "Entrar", command= exibirMensagem)
entrar.pack()

sair = Button(janela, text= "Sair", command= janela.destroy)
sair.pack()
janela.mainloop()