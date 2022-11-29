import tkinter as tk
from tkinter import messagebox
from tkinter import IntVar
from usuario import *
from aluno import *

class Principal (tk.Frame):
    def __init__(self):
        self.telaLogin()
        self.master.geometry("650x700")
        self.master.title("Controle de alunos e notas")
        self.radioMatricula = tk.Radiobutton()
        self.radioNome = tk.Radiobutton()
        self.campoTermo = tk.Entry()
        self.labelMotivo = tk.Label()
        self.campoMotivo = tk.Entry()
        self.escolha = tk.IntVar()
        self.campoListaAlunos = tk.Text()

    def telaLogin(self):
        tk.Frame.__init__(self)
        self.labelMenu = tk.Label(self.master,text="Login",font="Arial 18")
        self.labelMenu.grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoEfetuarLogin = tk.Button(self.master,text="Login Usuário",font="Arial 14",command = lambda: self.iniciaLoginUsuario())
        self.botaoEfetuarLogin.grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoCriarLogin = tk.Button(self.master,text="Criar Usuário",font="Arial 14",command = lambda: self.iniciaCriarUsuario())
        self.botaoCriarLogin.grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoSair = tk.Button(self.master,text="Sair",bg="red",fg="white",font="Arial 14 bold",command=self.sair)
        self.botaoSair.grid(row=4,column=0,ipadx=20,ipady=20,padx=10,pady=20)
        
    def telaMenu(self):
        self.labelMenu = tk.Label(self.master,text="Menu",font="Arial 18")
        self.labelMenu.grid(row=0,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoIncluir = tk.Button(self.master,text="Incluir",font="Arial 14",command=self.telaIncluirAluno)
        self.botaoIncluir.grid(row=1,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoBuscar = tk.Button(self.master,text="Buscar",font="Arial 14",command=self.telaBuscarAluno)
        self.botaoBuscar.grid(row=2,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoListar = tk.Button(self.master,text="Listar",font="Arial 14",command=self.telaListarAluno)
        self.botaoListar.grid(row=3,column=0,ipadx=20,ipady=20,padx=10,pady=10)
        self.botaoSair = tk.Button(self.master,text="Sair",bg="red",fg="white",font="Arial 14 bold",command=self.sair)
        self.botaoSair.grid(row=4,column=0,ipadx=20,ipady=20,padx=10,pady=20)

    def iniciaLoginUsuario(self):
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
        self.botaoCriarLogin["state"] = "disabled"
        self.botaoEfetuarLogin["state"] = "disabled"
        self.labelTituloSecao = tk.Label(self.master,text="Novo usuário",font="Arial 18")
        self.labelTituloSecao.grid(row=0,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        self.labelLogin = tk.Label(self.master,text="Novo login: ",font="Arial 14")
        self.labelLogin.grid(row=1,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        self.labelSenha = tk.Label(self.master,text="Senha: ",font="Arial 14")
        self.labelSenha.grid(row=3,column=1,ipadx=10,ipady=10,padx=10,pady=10)
        self.entradaLogin = tk.Entry(self.master)
        self.entradaLogin.grid(row=2, column=1)
        self.entradaSenha = tk.Entry(self.master,show="*")
        self.entradaSenha.grid(row=4, column=1)
        self.botaoIncluir = tk.Button(self.master,text="Login",font="Arial 14",command = lambda: self.executaCriarUsuario(self.entradaLogin.get(),self.entradaSenha.get()))
        self.botaoIncluir.grid(row=5,column=1,ipadx=20,ipady=20,padx=10,pady=10)

    def executaCriarUsuario(self,login,senha):
        self.idUsuario = usuario.incluirUsuario (login,senha)
        if (self.idUsuario == -1):
            print("Usuário criado! Retorne e faça seu login.")
            tk.messagebox.showinfo (title="Sucesso", message="Usuário criado! Retorne e faça seu login.")
            self.botaoCriarLogin["state"] = "active"
            self.botaoEfetuarLogin["state"] = "active"
            self.labelTituloSecao.destroy()
            self.labelLogin.destroy()
            self.labelSenha.destroy()
            self.entradaLogin.destroy()
            self.entradaSenha.destroy()
            self.botaoIncluir.destroy()
        else:
            tk.messagebox.showerror(title="Erro", message="Erro ao criar usuário")

    def telaAluno(self):
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

    def telaIncluirAluno(self):
        self.botaoIncluir["state"] = "disabled"
        self.botaoBuscar["state"] = "disabled"
        self.botaoListar["state"] = "disabled"
        self.telaAluno()
        self.labelTituloSecao = tk.Label(self.master,text="Incluir aluno",font="Arial 18")
        self.labelTituloSecao.grid(row=0,column=1,padx=5,pady=5)
        self.botaoGravarBuscar = tk.Button(self.master,text="Gravar",bg="green",fg="white",font="Arial 14",command=self.executaIncluirAluno)
        self.botaoGravarBuscar.grid(row=7,column=1,ipadx=2,ipady=2,padx=10,pady=10)
        self.botaoVoltar = tk.Button(self.master,text="Voltar",font="Arial 14 bold",command=self.executaDesfazTelaAluno)
        self.botaoVoltar.grid(row=7,column=2,ipadx=2,ipady=2,padx=10,pady=20)

    def executaIncluirAluno(self):
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
            tk.messagebox.showerror(title="Erro", message="Erro ao incluir aluno.")

    def telaBuscarAluno(self):
        self.botaoIncluir["state"] = "disabled"
        self.botaoBuscar["state"] = "disabled"
        self.botaoListar["state"] = "disabled"
        self.labelTituloSecao = tk.Label(self.master,text="Buscar aluno",font="Arial 18")
        self.labelTituloSecao.grid(row=0,column=1,padx=5,pady=5)
        self.labelEscolha = tk.Label(self.master,text="Como desejar buscar?",font="Arial 14")
        self.labelEscolha.grid(row=1,column=1,ipadx=20,ipady=20,padx=10,pady=10)
        self.radioMatricula = tk.Radiobutton(self.master, text="Matrícula", variable=self.escolha,value=1)
        self.radioMatricula.grid(row=2,column=1)
        self.radioNome = tk.Radiobutton(self.master, text="Nome", variable=self.escolha,value=2)
        self.radioNome.grid(row=3,column=1)
        self.escolha.set(1)
        self.campoTermo = tk.Entry(self.master,width=20)
        self.campoTermo.grid(row=4,column=1)
        self.botaoGravarBuscar = tk.Button(self.master,text="Buscar",font="Arial 14",command=self.executaBuscarAluno)
        self.botaoGravarBuscar.grid(row=7,column=1,ipadx=2,ipady=2,padx=10,pady=10)

    def executaBuscarAluno(self):
        self.termo = self.campoTermo.get()
        if(len(self.termo) == 0):
            tk.messagebox.showerror(title="Erro", message="Digite algum termo para buscar.")
        else:
            self.retornoAluno = aluno.buscarAluno(int(self.escolha.get()),str(self.termo))
            if(self.retornoAluno != None):
                self.labelEscolha.destroy()
                self.radioMatricula.destroy()
                self.radioNome.destroy()
                self.campoTermo.destroy()
                self.botaoGravarBuscar.destroy()
                self.labelTituloSecao.config(text = 'Consultar e Alterar aluno')
                self.telaAluno()
                self.campoMatricula.delete(0, 'end')
                self.campoMatricula.insert(0,str(self.retornoAluno[0]))
                self.campoMatricula.config(state= "disabled")
                self.campoNome.delete(0, 'end')
                self.campoNome.insert(0,str(self.retornoAluno[1]))
                self.campoNome.config(state= "disabled")
                self.campoAV1.delete(0, 'end')
                self.campoAV1.insert(0,str(self.retornoAluno[2]))
                self.campoAV2.delete(0, 'end')
                self.campoAV2.insert(0,str(self.retornoAluno[3]))
                self.campoAV3.delete(0, 'end')
                self.campoAV3.insert(0,str(self.retornoAluno[4]))
                self.campoAV4.delete(0, 'end')
                self.campoAV4.insert(0,str(self.retornoAluno[5]))
                self.labelMotivo = tk.Label(self.master,text="Motivo da alteração: ",fg="red",font="Arial 12")
                self.labelMotivo.grid(row=8,column=1)
                self.campoMotivo = tk.Entry(self.master,width=20)
                self.campoMotivo.grid(row=8,column=2)
                self.botaoGravarBuscar = tk.Button(self.master,text="Gravar",bg="green",fg="white",font="Arial 14",command=self.executaAlterarAluno)
                self.botaoGravarBuscar.grid(row=9,column=1,ipadx=2,ipady=2,padx=10,pady=10)
                self.botaoVoltar = tk.Button(self.master,text="Voltar",font="Arial 14 bold",command=self.executaDesfazTelaAluno)
                self.botaoVoltar.grid(row=9,column=2,ipadx=2,ipady=2,padx=10,pady=20)
            else:
                tk.messagebox.showerror(title="Erro", message="Aluno não encontrado. Refaça sua busca.")

    def executaAlterarAluno(self):
        if(
            float(self.retornoAluno[2]) != float(self.campoAV1.get()) or
            float(self.retornoAluno[3]) != float(self.campoAV2.get()) or
            float(self.retornoAluno[4]) != float(self.campoAV3.get()) or
            float(self.retornoAluno[5]) != float(self.campoAV4.get()) ):
            print("Houve alteração")
            if(len(self.campoMotivo.get()) == 0):
                tk.messagebox.showerror(title="Erro", message="Insira um motivo para a alteração e tente novamente. Nada foi gravado.")
            else:
                print("Realizar alteração")
                self.retornoAluno = aluno.alterarAluno(self.idUsuario,int(self.campoMatricula.get()),float(self.campoAV1.get()),float(self.campoAV2.get()),float(self.campoAV3.get()),self.campoAV4.get(),self.campoMotivo.get())
                if (self.retornoAluno == -1):
                    tk.messagebox.showinfo (title="Sucesso", message="Aluno alterado com sucesso.")
                else:
                    print("Erro ",self.retornoAluno)
                    tk.messagebox.showerror(title="Erro", message="Erro ao alterar aluno.")
        else:
            tk.messagebox.showinfo (title="Informação", message="Não houve alteração. Nada a ser gravado.")

    def executaDesfazTelaAluno(self):
        self.botaoIncluir["state"] = "normal"
        self.botaoBuscar["state"] = "normal"
        self.botaoListar["state"] = "normal"
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
        self.botaoGravarBuscar.destroy()
        self.botaoVoltar.destroy()
        self.labelMotivo.destroy()
        self.campoMotivo.destroy()

    def telaListarAluno(self):
        self.retornoAluno = aluno.listarAluno()
        if(self.retornoAluno == 0):
            tk.messagebox.showerror(title="Erro", message="Não há alunos para listar.")
            return 0
        self.botaoIncluir["state"] = "disabled"
        self.botaoBuscar["state"] = "disabled"
        self.botaoListar["state"] = "disabled"
        self.labelTituloSecao = tk.Label(self.master,text="Listar alunos",font="Arial 18")
        self.labelTituloSecao.grid(row=0,column=1,padx=5,pady=5)
        self.campoListaAlunos = tk.Text(self.master, width=60, height=len(self.retornoAluno)+1)
        self.campoListaAlunos.grid(row=2,column=1)
        for self.linha in self.retornoAluno:
            self.novaLinha = str(self.linha[0]) + '\t' + str(self.linha[1]) + '\t' + str(self.linha[2]) + '\t' + str(self.linha[3]) + '\n'
            self.campoListaAlunos.insert('end',self.novaLinha)
        self.botaoVoltar = tk.Button(self.master,text="Voltar",font="Arial 14 bold",command=self.executaDesfazTelaListar)
        self.botaoVoltar.grid(row=10,column=1,ipadx=2,ipady=2,padx=10,pady=20)

    def executaDesfazTelaListar(self):
        self.botaoIncluir["state"] = "normal"
        self.botaoBuscar["state"] = "normal"
        self.botaoListar["state"] = "normal"
        self.labelTituloSecao.destroy()
        self.campoListaAlunos.destroy()
        self.botaoVoltar.destroy()

    def sair(self):
        tk.messagebox.showinfo(title="Tchau!", message="Criado por Luiz Gabriel Garcia e Marcel Luiz Michalovsky Oliveira.")
        Principal.quit(self)
        print("Aplicativo encerrado.")

idUsuario = None
retornoAluno = None
usuario = Usuario()
usuario.instalaBanco()
aluno = Aluno()
obj = Principal()
obj.mainloop()