from tkinter import *
from tkinter import messagebox

janela = Tk()

janela.title("Minha Primeira Janela")  # nomeando a janela
janela.geometry("600x600+630+200")  # tamanho + posição
janela.minsize(200, 200)  # tamanho mínimo da tela
janela.maxsize(600, 600)  # tamanho máximo da tela
janela.resizable(False, False)  # bloqueando redimensionar a tela
#janela.state("zoomed")  # começar a tela maximizada
#janela.state("iconic")  # começar a tela minimizada
janela['bg'] = "grey"  # mudar a cor de fundo da janela

# Funções
def mensagem1():
    texto = txtnome.get()
    print(texto)

def mensagem2():
    messagebox.showinfo("Informação!!", "Mensagem de informação")

def mensagem3():
    messagebox.showwarning("Atenção!!", "Mensagem de aviso")

def mensagem4():
    messagebox.showerror("Erro!!", "Mensagem de erro")

# Adicionar uma label
nome = Label(janela, text="Nome", font="Arial 20", bg="grey", fg="black")
nome.pack(pady=10)

# Adicionar caixa de texto
txtnome = Entry(janela, font="Arial 20", bg="white", fg="black", bd=2, relief="solid")
txtnome.pack(pady=10)

# Definir a largura e altura dos botões para garantir que todos tenham o mesmo tamanho
button_width = 10  # Largura de cada botão
button_height = 1  # Altura de cada botão

# Adicionando botões
bota1 = Button(janela, text="Clique aqui!", font="Arial 20", command=mensagem1, bd=2, relief="solid", width=button_width, height=button_height)
bota1.pack(pady=10)

bota2 = Button(janela, text="AVISO!", font="Arial 20", command=mensagem2, bd=2, relief="solid", width=button_width, height=button_height)
bota2.pack(pady=10)

bota3 = Button(janela, text="Atenção!", font="Arial 20", command=mensagem3, bd=2, relief="solid", width=button_width, height=button_height)
bota3.pack(pady=10)

bota4 = Button(janela, text="ERRO!", font="Arial 20", command=mensagem4, bd=2, relief="solid", width=button_width, height=button_height)
bota4.pack(pady=10)

# Rodando a interface gráfica
janela.mainloop()
