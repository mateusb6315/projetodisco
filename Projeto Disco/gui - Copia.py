from tkinter import *
from tkinter import ttk
import db
from tkinter import messagebox

def mostrar_sobre():        
    sobrejanela = Toplevel()
    sobrejanela.title("Sobre")

    info = Label(sobrejanela, text="Versão alfa 0.1")
    info.pack(padx=30, pady=30)

class App:
    def __init__(self, master=None):

        # primeiro container
        self.fonte = ("Arial", "10")
        self.mestre = Frame(master)
        self.mestre["pady"] = 10
        self.mestre.pack()

        # segundo container
        self.container2 = Frame(master)
        self.container2["padx"] = 30
        self.container2["pady"] = 10
        self.container2.pack()

        # terceiro container

        self.container3 = Frame(master)
        self.container3["padx"] = 30
        self.container3["pady"] = 20
        self.container3.pack()

        # quarto container

        self.container4 = Frame(master)
        self.container4["pady"] = 20
        self.container4.pack()

        # título e inserção
        self.titulo = Label(self.mestre, text="Projeto Disco:")
        self.titulo["font"] = ("Arial", "12", "italic", "bold")
        self.titulo.pack()

        self.idprod = Label(self.container2, text="ID:")
        self.idprod["width"] = 2
        self.idprod["font"] = self.fonte
        self.idprod.pack(side=LEFT)

        self.busca = Entry(self.container2)
        self.busca["font"] = self.fonte
        self.busca.pack(side=LEFT)

        self.espaco = Label(self.container2, text=" ")
        self.espaco.pack(side=LEFT)

        self.nome = Label(self.container2, text="Palavra-chave:")
        self.idprod["width"] = 2
        self.nome["font"] = self.fonte
        self.nome.pack(side=LEFT)

        self.busca2 = Entry(self.container2)
        self.busca2["font"] = self.fonte
        self.busca2.pack(side=RIGHT)

        # botão de pesquisa
        self.pesquisar = Button(self.container4)
        self.pesquisar["text"] = "Pesquisar"
        self.pesquisar["font"] = self.fonte
        self.pesquisar["width"] = 25
        self.pesquisar["command"] = self.realizar_pesquisa
        self.pesquisar.pack()

        # tabela
        self.frametabela = Frame(self.container4)
        self.frametabela.pack(pady=10)
        self.tabela = ttk.Treeview(self.container4, columns=("ID", "Produto", "Preço"))
        self.tabela["show"] = "headings"
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Produto", text="Produto")
        self.tabela.heading("Preço", text="Preço")

        self.tabela.place(relwidth=0.7, relheight=1, relx=0.1)

        self.tabela.column("ID", width=50)
        self.tabela.column("Produto", width=200)
        self.tabela.column("Preço", width=80)

        self.tabela.tag_configure("center", anchor="center")
        self.tabela.heading("ID", text="ID", anchor="center", command=lambda: self.sort_column(self.tabela, "ID", False))
        self.tabela.column("ID", anchor="center")

        self.tabela.tag_configure("center", anchor="center")
        self.tabela.heading("Produto", text="Produto", anchor="center", command=lambda: self.sort_column(self.tabela, "Produto", False))
        self.tabela.column("Produto", anchor="center")

        self.tabela.tag_configure("center", anchor="center")
        self.tabela.heading("Preço", text="Preço", anchor="center", command=lambda: self.sort_column(self.tabela, "Preço", False))
        self.tabela.column("Preço", anchor="center")

        self.tabela.pack()

    def realizar_pesquisa(self):
        id_valor = self.busca.get()
        key_valor = self.busca2.get()

        conexao = db.conectar_db()

        if conexao is not None:
            consulta = ""
            parametros = ()

            if id_valor.isdigit():
             consulta = "SELECT id, nome, valor FROM produto WHERE id = %s"
             parametros = (id_valor,)

            else:
             consulta = "SELECT id, nome, valor FROM produto WHERE nome ILIKE %s"
             parametros = (f'%{key_valor}%',)

            resultados = db.busca(conexao, consulta, parametros)

            conexao.close()

            for item in self.tabela.get_children():
                self.tabela.delete(item)

            for resultado in resultados:
                self.tabela.insert("", "end", values=resultado)

        else:
            messagebox.showerror("Erro", "Não foi possível se conectar ao banco de dados")


janela = Tk()
janela.title("Projeto Disco")
app = App(janela)
janela.mainloop()