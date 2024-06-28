import tkinter as tk
from tkinter import ttk

#Configuração da janela
window = tk.Tk()
window.title('GI - SESMT')
window.rowconfigure([0, 1, 2, 3], minsize=10, weight=1)
window.columnconfigure([0, 1, 2, 3, 4], minsize=20, weight=1)

#Head
lbl_head = tk.Label(master=window, text='Gestão Informacional - SESMT', font=('Arial', 23))
lbl_head.grid(row=0,column=2,sticky=tk.N)

#rótulo da secretaria
lbl_secretaria = tk.Label(master=window, text='Escolha a Secretaria:', font=('Arial', 16))
lbl_secretaria.grid(row=1, column=0, sticky=tk.NW)

#Menu com as secretarias
lista_secretarias = ['Sec A', 'Sec B', 'Sec C', 'Sec D']
valor_optmenu_secretaria = tk.StringVar(window) 
valor_optmenu_secretaria.set("Selecione uma Opção:") 
optmenu_secretaria = tk.OptionMenu(window, valor_optmenu_secretaria, *lista_secretarias) 
optmenu_secretaria.grid(row=1, column=2, sticky=tk.NW) 

#rótulo da instituição
lbl_instituicao = tk.Label(master=window, text='Escolha a Instituição:', font=('Arial', 16))
lbl_instituicao.grid(row=1, column=2, sticky=tk.NE)

#Menu com as instituições
lista_instituicoes = ['Inst A', 'Inst B', 'Inst C', 'Inst D']
valor_optmenu_instituicao = tk.StringVar(window) 
valor_optmenu_instituicao.set("Selecione uma Opção:") 
optmenu_instituicao = tk.OptionMenu(window, valor_optmenu_instituicao, *lista_instituicoes) 
optmenu_instituicao.grid(row=1, column=3, sticky=tk.NW)

#Menu com Grupos de exposição
lista_instituicoes = ['GP A', 'GP B', 'GP C', 'Inst D']
valor_optmenu_instituicao = tk.StringVar(window) 
valor_optmenu_instituicao.set("Selecione uma Opção:") 
optmenu_instituicao = tk.OptionMenu(window, valor_optmenu_instituicao, *lista_instituicoes) 
optmenu_instituicao.grid(row=1, column=3, sticky=tk.NW)

window.mainloop()
