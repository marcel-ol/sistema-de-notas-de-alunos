import tkinter as tk
# import psycopg2 as pg
from usuario import *
from tkinter import messagebox

class Principal (tk.Frame):
    idUsuario = None

    def __init__(self):
        self.telaLogin()
        self.master.geometry("1000x600")
        self.master.title("Controle de alunos e notas")

    def telaLogin(self):
        tk.Frame.__init__(self)
        self.label1 = tk.Label(self.master,text="Login",font="Arial 18")
        self.label1.grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoEfetuarLogin = tk.Button(self.master,text="Login Usuário",font="Arial 14",command = lambda: self.iniciaLoginUsuario())
        self.botaoEfetuarLogin.grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoCriarLogin = tk.Button(self.master,text="Criar Usuário",font="Arial 14",command = lambda: self.iniciaCriarUsuario())
        self.botaoCriarLogin.grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        # self.botaoVoltar = tk.Button(self.master,text="Sair",bg="red",fg="white",font="Arial 14 bold",command = lambda: self.limparTelaLogin('botaoCriarLogin'))
        # self.botaoVoltar.grid(row=5,column=0,ipadx=20,ipady=20,padx=10,pady=20)
        self.botaoSair = tk.Button(self.master,text="Sair",bg="red",fg="white",font="Arial 14 bold",command=self.sair)
        self.botaoSair.grid(row=3,column=0,ipadx=20,ipady=20,padx=10,pady=20)
        
    
    def telaMenu(self):
        labelMenu = tk.Label(self.master,text="Menu",font="Arial 18")
        labelMenu.grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        botaoIncluir = tk.Button(self.master,text="Incluir",font="Arial 14",command=self.incluir)
        botaoIncluir.grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        botaobuscar = tk.Button(self.master,text="Buscar",font="Arial 14",command=self.buscar)
        botaobuscar.grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        botaoSair = tk.Button(self.master,text="Sair",bg="red",fg="white",font="Arial 14 bold",command=self.sair)
        botaoSair.grid(row=4,column=0,ipadx=20,ipady=20,padx=10,pady=20)

    def iniciaLoginUsuario(self):
        print("iniciaLoginUsuario")
        self.botaoCriarLogin["state"] = "disabled"
        self.botaoEfetuarLogin["state"] = "disabled"
        self.labelTituloSecao = tk.Label(self.master,text="Efetuar login",font="Arial 18")
        self.labelTituloSecao.grid(row=0,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        self.labelLogin = tk.Label(self.master,text="Login: ",font="Arial 14")
        self.labelLogin.grid(row=1,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        self.labelSenha = tk.Label(self.master,text="Senha: ",font="Arial 14")
        self.labelSenha.grid(row=3,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        self.entradaLogin = tk.Entry(self.master)
        self.entradaLogin.grid(row=2, column=1)
        self.entradaSenha = tk.Entry(self.master,show="*")
        self.entradaSenha.grid(row=4, column=1)
        self.botaoIncluir = tk.Button(self.master,text="Login",font="Arial 14",command = lambda: self.executaLoginUsuario(self.entradaLogin.get(),self.entradaSenha.get()))
        self.botaoIncluir.grid(row=5,column=1,ipadx=20,ipady=20,padx=10,pady=10)

    def executaLoginUsuario(self,login,senha):
        self.idUsuario = usuario.loginUsuario(login,senha)
        if (self.idUsuario == 0):
            tk.messagebox.showerror(title="Erro", message="Usuário/senha não conferem.")
        else:
            print("login ok")
            self.labelTituloSecao.destroy()
            self.labelLogin.destroy()
            self.labelSenha.destroy()
            self.entradaLogin.destroy()
            self.entradaSenha.destroy()
            self.botaoIncluir.destroy()
            self.botaoCriarLogin.destroy()
            self.botaoEfetuarLogin.destroy()
            self.botaoSair.destroy()
            self.label1.destroy()
            self.telaMenu()

    def iniciaCriarUsuario(self):
        print("iniciaLoginUsuario")
        self.botaoCriarLogin["state"] = "disabled"
        self.botaoEfetuarLogin["state"] = "disabled"
        labelTituloSecao = tk.Label(self.master,text="Novo usuário",font="Arial 18")
        labelTituloSecao.grid(row=0,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        labelLogin = tk.Label(self.master,text="Novo login: ",font="Arial 14")
        labelLogin.grid(row=1,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        labelSenha = tk.Label(self.master,text="Senha: ",font="Arial 14")
        labelSenha.grid(row=3,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        entradaLogin = tk.Entry(self.master)
        entradaLogin.grid(row=2, column=1)
        entradaSenha = tk.Entry(self.master,show="*")
        entradaSenha.grid(row=4, column=1)
        botaoIncluir = tk.Button(self.master,text="Login",font="Arial 14",command = lambda: self.executaCriarUsuario(entradaLogin.get(),entradaSenha.get()))
        botaoIncluir.grid(row=5,column=1,ipadx=20,ipady=20,padx=10,pady=10)

    def executaCriarUsuario(self,login,senha):
        self.idUsuario = usuario.incluirUsuario (login,senha)
        if (self.idUsuario == 0):
            tk.messagebox.showerror(title="Erro", message="Erro ao criar usuário")
        else:
            print("Usuário criado! Retorne e faça seu login.")
            print(self.idUsuario)
            self.botaoCriarLogin["state"] = "enabled"
            self.botaoEfetuarLogin["state"] = "enabled"

    def buscar(self):
        print("buscar")
    def incluir(self):
        print("Incluir")
    def sair(self):
        Principal.quit(self)
        print("Aplicativo encerrado.")
usuario = Usuario()
usuario.instalaBanco()
obj = Principal()
obj.mainloop()