from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk()
janela.geometry("950x350")
janela.title("TreeView")

id = Label(text= "ID", font= "Arial 12")
id.grid(row=1, column=0, stick="W")
campoDigitavelID = Entry(font="Arial 12")
campoDigitavelID.grid(row=1, column=1, stick="W")

nome = Label(text= "Nome", font= "Arial 12")
nome.grid(row=1, column=2, stick="W")
campoDigitavelNome = Entry(font="Arial 12")
campoDigitavelNome.grid(row=1, column=3, stick="W")

idade = Label(text= "Idade", font= "Arial 12")
idade.grid(row=1, column=4, stick="W")
campoDigitavelIdade = Entry(font="Arial 12")
campoDigitavelIdade.grid(row=1, column=5, stick="W")

sexo = Label(text= "Sexo", font= "Arial 12")
sexo.grid(row=1, column=6, stick="W")
campoDigitavelSexo = Entry(font="Arial 12")
campoDigitavelSexo.grid(row=1, column=7, stick="W")

def addItemTreeview():
    treeViewDados.insert("", "end", 
                         values=(str(campoDigitavelID.get()), 
                                 str(campoDigitavelNome.get()),
                                 str(campoDigitavelIdade.get()),
                                 str(campoDigitavelSexo.get())
                                 ))
    campoDigitavelNome.delete(0, "end")
    campoDigitavelIdade.delete(0, "end")
    campoDigitavelSexo.delete(0, "end")
    campoDigitavelID.delete(0, "end")

botaoAdicionar = Button(text="Cadastrar",
                        font= "Arial 20",
                        command= addItemTreeview)
botaoAdicionar.grid(row=2, column=0, columnspan=4, stick="NSEW")

estiloJanela = ttk.Style()
estiloJanela.theme_use("alt")
estiloJanela.configure(".", font = "Arial 14")

treeViewDados = ttk.Treeview(janela, column=(1, 2, 3, 4), show="headings")

treeViewDados.column("1", anchor=CENTER)
treeViewDados.heading("1", text="ID")

treeViewDados.column("2", anchor=CENTER)
treeViewDados.heading("2", text="Nome")

treeViewDados.column("3", anchor=CENTER)
treeViewDados.heading("3", text="Idade")

treeViewDados.column("4", anchor=CENTER)
treeViewDados.heading("4", text="Sexo")

treeViewDados.insert("", "end", text="1", values=("1", "Allan", 29, "Masculino"))
treeViewDados.insert("", "end", text="2", values=("2", "Ana", 41, "Feminino"))
treeViewDados.insert("", "end", text="3", values=("3", "Berenice", 50, "Feminino"))
treeViewDados.insert("", "end", text="4", values=("4", "Roger", 19, "Masculino"))
treeViewDados.insert("", "end", text="5", values=("5", "Pedro", 25, "Masculino"))

treeViewDados.grid(row=3, column=0, columnspan=8, stick="NSEW")

botaoDeletar = Button(text="Deletar",
                        font= "Arial 20",
                        command= addItemTreeview)
botaoDeletar.grid(row=2, column=4, columnspan=4, stick="NSEW")

janela.mainloop()