import tkinter as tk
from tkinter import messagebox
from usuario import *
from aluno import *

class Principal (tk.Frame):
    idUsuario = None
    retornoAluno = None
    def __init__(self):
        self.telaLogin()
        self.master.geometry("1000x600")
        self.master.title("Controle de alunos e notas")

    def telaLogin(self):
        tk.Frame.__init__(self)
        self.labelMenu = tk.Label(self.master,text="Login",font="Arial 18")
        self.labelMenu.grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoEfetuarLogin = tk.Button(self.master,text="Login Usuário",font="Arial 14",command = lambda: self.iniciaLoginUsuario())
        self.botaoEfetuarLogin.grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoCriarLogin = tk.Button(self.master,text="Criar Usuário",font="Arial 14",command = lambda: self.iniciaCriarUsuario())
        self.botaoCriarLogin.grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        # self.botaoVoltar = tk.Button(self.master,text="Sair",bg="red",fg="white",font="Arial 14 bold",command = lambda: self.limparTelaLogin('botaoCriarLogin'))
        # self.botaoVoltar.grid(row=5,column=0,ipadx=20,ipady=20,padx=10,pady=20)
        self.botaoSair = tk.Button(self.master,text="Sair",bg="red",fg="white",font="Arial 14 bold",command=self.sair)
        self.botaoSair.grid(row=3,column=0,ipadx=20,ipady=20,padx=10,pady=20)
        
    
    def telaMenu(self):
        self.labelMenu = tk.Label(self.master,text="Menu",font="Arial 18")
        self.labelMenu.grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoIncluir = tk.Button(self.master,text="Incluir",font="Arial 14",command=self.telaIncluir)
        self.botaoIncluir.grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoBuscar = tk.Button(self.master,text="Buscar",font="Arial 14",command=self.buscar)
        self.botaoBuscar.grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoSair = tk.Button(self.master,text="Sair",bg="red",fg="white",font="Arial 14 bold",command=self.sair)
        self.botaoSair.grid(row=4,column=0,ipadx=20,ipady=20,padx=10,pady=20)

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
            self.labelTituloSecao.destroy()
            self.labelLogin.destroy()
            self.labelSenha.destroy()
            self.entradaLogin.destroy()
            self.entradaSenha.destroy()
            self.botaoIncluir.destroy()
            self.botaoCriarLogin.destroy()
            self.botaoEfetuarLogin.destroy()
            self.botaoSair.destroy()
            self.labelMenu.destroy()
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
        if (self.idUsuario == -1):
            print("Usuário criado! Retorne e faça seu login.")
            print(self.idUsuario)
            self.botaoCriarLogin["state"] = "active"
            self.botaoEfetuarLogin["state"] = "active"
            self.labelTituloSecao.destroy()
            self.labelLogin.destroy()
            self.labelSenha.destroy()
            self.entradaLogin.destroy()
            self.entradaSenha.destroy()
        else:
            tk.messagebox.showerror(title="Erro", message="Erro ao criar usuário")

    def buscar(self):
        print("buscar")
    def telaIncluir(self):
        print("telaIncluir")
        self.botaoIncluir["state"] = "disabled"
        self.botaoBuscar["state"] = "disabled"
        self.labelTituloSecao = tk.Label(self.master,text="Incluir aluno",font="Arial 18")
        self.labelTituloSecao.grid(row=0,column=1,padx=5,pady=5)
        self.labelMatricula = tk.Label(self.master,text="Matrícula (somente números):",font="Arial 12")
        self.labelMatricula.grid(row=1,column=1)
        self.campoMatricula = tk.Entry(self.master)
        self.campoMatricula.grid(row=1,column=2)
        self.labelNome = tk.Label(self.master,text="Nome:",font="Arial 12")
        self.labelNome.grid(row=2,column=1)
        self.campoNome = tk.Entry(self.master)
        self.campoNome.grid(row=2,column=2)
        self.labelAV1 = tk.Label(self.master,text="Nota AV1:",font="Arial 12")
        self.labelAV1.grid(row=3,column=1)
        self.campoAV1 = tk.Entry(self.master)
        self.campoAV1.grid(row=3,column=2)
        self.labelAV2 = tk.Label(self.master,text="Nota AV2:",font="Arial 12")
        self.labelAV2.grid(row=4,column=1)
        self.campoAV2 = tk.Entry(self.master)
        self.campoAV2.grid(row=4,column=2)
        self.labelAV3 = tk.Label(self.master,text="Nota AV3:",font="Arial 12")
        self.labelAV3.grid(row=5,column=1,padx=5,pady=5)
        self.campoAV3 = tk.Entry(self.master)
        self.campoAV3.grid(row=5,column=2,padx=5,pady=5)
        self.labelAV4 = tk.Label(self.master,text="Nota AV4:",font="Arial 12")
        self.labelAV4.grid(row=6,column=1,padx=5,pady=5)
        self.campoAV4 = tk.Entry(self.master)
        self.campoAV4.grid(row=6,column=2,padx=5,pady=5)
        self.botaoGravar = tk.Button(self.master,text="Gravar",bg="green",fg="white",font="Arial 14",command=self.executaIncluirAluno)
        self.botaoGravar.grid(row=7,column=1,ipadx=2,ipady=2,padx=10,pady=10)
        self.botaoVoltar = tk.Button(self.master,text="Voltar",font="Arial 14 bold",command=self.executaVoltar)
        self.botaoVoltar.grid(row=7,column=2,ipadx=2,ipady=2,padx=10,pady=20)

    def executaIncluirAluno(self):
        print("executaIncluirAluno")
        self.retornoAluno = aluno.incluirAluno(self.idUsuario,self.campoNome.get(),self.campoMatricula.get(),self.campoAV1.get(),self.campoAV2.get(),self.campoAV3.get(),self.campoAV4.get())
        if (self.retornoAluno == -1):
            tk.messagebox.showinfo (title="Sucesso", message="Aluno incluído com sucesso.")
            self.campoMatricula.delete(0, 'end')
            self.campoNome.delete(0, 'end')
            self.campoAV1.delete(0, 'end')
            self.campoAV2.delete(0, 'end')
            self.campoAV3.delete(0, 'end')
            self.campoAV4.delete(0, 'end')
        else:
            print("Erro ",self.retornoAluno)
            tk.messagebox.showerror(title="Erro", message="Erro ao incluir aluno.")
            
    def executaVoltar(self):
        print("executaVoltar")
        self.botaoIncluir["state"] = "normal"
        self.botaoBuscar["state"] = "normal"
        self.labelTituloSecao.destroy()
        self.labelMatricula.destroy()
        self.campoMatricula.destroy()
        self.labelNome.destroy()
        self.campoNome.destroy()
        self.labelAV1.destroy()
        self.campoAV1.destroy()
        self.labelAV2.destroy()
        self.campoAV2.destroy()
        self.labelAV3.destroy()
        self.campoAV3.destroy()
        self.labelAV4.destroy()
        self.campoAV4.destroy()
        self.botaoGravar.destroy()
        self.botaoVoltar.destroy()

    def sair(self):
        Principal.quit(self)
        print("Aplicativo encerrado.")
usuario = Usuario()
usuario.instalaBanco()
aluno = Aluno()
obj = Principal()
obj.mainloop()