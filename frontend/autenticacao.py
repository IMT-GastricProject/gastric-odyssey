import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

class Autenticacao(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tela_login()

    #Configurando a janela principal
    def configuracoes_da_janela_inicial(self):
        self.geometry("450x430")
        self.title('Tela de login e cadastro')
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        self.iconbitmap('asstes/menu/Burger.ico')
        
    #Tela de login
    def tela_login(self):

        #Criar frame do formulário de login
        self.frame_login = ctk.CTkFrame(self, width=500, height=700, fg_color="gray30")
        self.frame_login.place(x=15, y=55)

        #Título da plataforma de login
        self.title = ctk.CTkLabel(self, text="Acessar menu do jogo", font=("Century Gothic", 24))
        self.title.grid(row=0, column=0, padx=83, pady=10)

        #Colocar widgets dentro do frame
        self.lb_title = ctk.CTkLabel(self.frame_login, text="Login", font=("Century Gothic", 20))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)

        #Espaço para inserir nome de usuário
        self.nome_login_entry = ctk.CTkEntry(self.frame_login, width=400, placeholder_text="Nome de usuário", font=("Century Gothic", 14), corner_radius=15)
        self.nome_login_entry.grid(row=1, column=0, padx=10, pady=10)
    
        #Espaço para inserir e-mail
        self.email_login_entry = ctk.CTkEntry(self.frame_login, width=400, placeholder_text="E-mail institucional", font=("Century Gothic", 14), corner_radius=15)
        self.email_login_entry.grid(row=2, column=0, padx=10, pady=10)

        #Espaço para inserir senha
        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=400, placeholder_text="Senha", font=("Century Gothic", 14), corner_radius=15, show="*")
        self.senha_login_entry.grid(row=3, column=0, padx=10, pady=10)

        #Opção ver senha
        self.ver_senha_login = ctk.CTkCheckBox(self.frame_login, text="Ver senha", font=("Century Gothic", 14), border_color="steelblue3", command=self.toggle_password_login)
        self.ver_senha_login.grid(row=4, column=0, padx=10, pady=10)

        #Botão de login
        self.botao_login = ctk.CTkButton(self.frame_login, width=200, text="Entrar", font=("Century Gothic", 14), corner_radius=15, command=self.limpa_entry_login)
        self.botao_login.grid(row=5, column=0, padx=10, pady=10)

        #Opção "se não possuir cadastro"
        self.spam = ctk.CTkLabel(self.frame_login, text="Não possui cadastro?", font=("Century Gothic", 12))
        self.spam.grid(row=6, column=0, padx=10, pady=10)

        #Botão de ir para tela de cadastro
        self.botao_sem_cadastro = ctk.CTkButton(self.frame_login, width=30, fg_color="gray30", hover_color="gray40", text_color="white", text="Cadastre-se", font=("Century Gothic", 14), corner_radius=15, command=self.tela_cadastro)
        self.botao_sem_cadastro.grid(row=7, column=0, padx=0, pady=0)

    # Função para alternar a visibilidade da senha durante o login
    def toggle_password_login(self):
        if self.ver_senha_login.get() == 1:  # Verifica se o CheckButton está marcado
            self.senha_login_entry.configure(show="")
        else:
            self.senha_login_entry.configure(show="*")

    def tela_cadastro(self):
        # Remover o frame de cadastro, se estiver visível
        if hasattr(self, 'frame_cadastro') and self.frame_cadastro.winfo_exists():
            self.frame_cadastro.place_forget()

        #Remover o formulário de login
        self.frame_login.place_forget()

        #Criar frame do formulário de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=500, height=700, fg_color="gray30")
        self.frame_cadastro.place(x=15, y=55)

        #Colocar widgets dentro do frame
        self.lb_title = ctk.CTkLabel(self.frame_cadastro, text="Cadastro", font=("Century Gothic", 20))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)
        
        #Espaço para inserir novo nome de usuário
        self.nome_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=400, placeholder_text="Nome de usuário", font=("Century Gothic", 14), corner_radius=15)
        self.nome_cadastro_entry.grid(row=1, column=0, padx=10, pady=10)
    
        #Espaço para inserir novo e-mail
        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=400, placeholder_text="E-mail institucional", font=("Century Gothic", 14), corner_radius=15)
        self.email_cadastro_entry.grid(row=2, column=0, padx=10, pady=10)

        #Espaço para inserir nova senha
        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=400, placeholder_text="Senha", font=("Century Gothic", 14), corner_radius=15, show="*")
        self.senha_cadastro_entry.grid(row=3, column=0, padx=10, pady=10)

        #Opção ver senha
        self.ver_senha_cadastro = ctk.CTkCheckBox(self.frame_cadastro, text="Ver senha", font=("Century Gothic", 14), border_color="steelblue3", command=self.toggle_password_cadastro)
        self.ver_senha_cadastro.grid(row=4, column=0, padx=10, pady=10)

        #Botão de cadastro
        self.botao_cadastro = ctk.CTkButton(self.frame_cadastro, width=200, text="Cadastrar-se", font=("Century Gothic", 14), corner_radius=15, command=self.tela_codigo_verificacao)
        self.botao_cadastro.grid(row=5, column=0, padx=10, pady=10)

        #Opção "se já possuir cadastro"
        self.spam = ctk.CTkLabel(self.frame_cadastro, text="Já possui cadastro?", font=("Century Gothic", 12))
        self.spam.grid(row=6, column=0, padx=10, pady=10)

        #Botão de ir para tela de login
        self.botao_com_login = ctk.CTkButton(self.frame_cadastro, width=30, fg_color="gray30", hover_color="gray40", text_color="white", text="Login", font=("Century Gothic", 14), corner_radius=15, command=self.tela_login)
        self.botao_com_login.grid(row=7, column=0, padx=0, pady=0)

    # Função para alternar a visibilidade da senha durante o cadastro
    def toggle_password_cadastro(self):
        if self.ver_senha_cadastro.get() == 1:  # Verifica se o CheckButton está marcado
            self.senha_cadastro_entry.configure(show="")
        else:
            self.senha_cadastro_entry.configure(show="*")
    
    #Tela de código de verificação
    def tela_codigo_verificacao(self):
        #Remover o formulário de cadastro
        self.frame_cadastro.place_forget()

        #Criar frame do formulário de cadastro
        self.frame_codigo = ctk.CTkFrame(self, width=500, height=700, fg_color="gray30")
        self.frame_codigo.place(x=15, y=55)

        #Colocar widgets dentro do frame
        self.lb_title = ctk.CTkLabel(self.frame_codigo, text="Insira o código de verificação enviado \n para o seu e-mail", font=("Century Gothic", 20))
        self.lb_title.grid(row=0, column=0, padx=10, pady=10)
        
        #Espaço para inserir o código de  verificação
        self.nome_codigo_entry = ctk.CTkEntry(self.frame_codigo, width=400, placeholder_text="Código de verificação", font=("Century Gothic", 14), corner_radius=15)
        self.nome_codigo_entry.grid(row=1, column=0, padx=10, pady=10)

        #Botão de confirmar
        self.botao_confirmar = ctk.CTkButton(self.frame_codigo, width=200, text="Confirmar", font=("Century Gothic", 14), corner_radius=15, command=self.limpa_entry_codigo)
        self.botao_confirmar.grid(row=5, column=0, padx=10, pady=10)

        #Botão de cancelar/voltar
        self.botao_cancelar = ctk.CTkButton(self.frame_codigo, width=30, fg_color="gray30", hover_color="gray40", text_color="white", text="Cancelar", font=("Century Gothic", 14), corner_radius=15, command=self.tela_cadastro)
        self.botao_cancelar.grid(row=7, column=0, padx=0, pady=0)

    #Limpar as entradas quando clicar no bootão
    def limpa_entry_cadastro(self):
        self.nome_cadastro_entry.delete(0,END)
        self.email_cadastro_entry.delete(0,END)
        self.senha_cadastro_entry.delete(0,END)

    def limpa_entry_login(self):
        self.nome_login_entry.delete(0,END)
        self.email_login_entry.delete(0,END)
        self.senha_login_entry.delete(0,END)

    def limpa_entry_codigo(self):
        self.nome_codigo_entry.delete(0,END)

if __name__=="__main__":
    app = Autenticacao()
    app.mainloop()