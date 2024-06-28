import tkinter as tk
from tkinter import ttk

#Configuração da janela
window = tk.Tk()
window.title('GI - SESMT')
window.state('zoomed')
#window_height = window.winfo_screenheight()
#window_width = window.winfo_screenwidth()
#center_x = int(window_width/16)
#center_y = int(window_height/16)
#window.geometry(f'{str(window_width)}x{str(window_height)}+{center_x}+{center_y}')
#window.geometry(f'1200x600+{center_x}+{center_y}')
#window.rowconfigure(0, weight=1)
#window.rowconfigure(1, weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)

#Frame para o cabeçalho
#frm_head = tk.Frame(master=window,bg='blue')
#frm_head.grid(row=0,column=0,columnspan=5)

#Head
lbl_head = tk.Label(master=window, text='Gestão Informacional - SESMT', font=('Arial', 23))
lbl_head.grid(row=0,column=0,sticky='n',columnspan=8)

#frame para as secs
frm_sec = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_sec.grid(row=1,column=0,columnspan=2,pady=20,sticky='w',padx=40)

#rótulo da secretaria
lbl_secretaria = tk.Label(master=frm_sec, text='Secretaria:', font=('Arial', 16))
lbl_secretaria.grid(row=1, column=0,sticky='w')

#Menu com as secretarias
lista_secretarias = ['Sec A', 'Sec B', 'Sec C', 'Sec D', 'Secretaria F']
valor_optmenu_secretaria = tk.StringVar(window) 
valor_optmenu_secretaria.set("Selecione uma Opção:") 
optmenu_secretaria = tk.OptionMenu(frm_sec, valor_optmenu_secretaria, *lista_secretarias) 
optmenu_secretaria.grid(row=1, column=1,sticky='e')

#frame para os grupos de Expo
frm_gpExpo = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_gpExpo.grid(row=1,column=2,columnspan=4,pady=20,sticky='n')

#rótulo grupo de exposição
lbl_gpExposicao = tk.Label(master=frm_gpExpo, text='Grupo de Exposição:', font=('Arial', 16))
lbl_gpExposicao.grid(row=1, column=2,sticky='w')

#Menu com Grupos de exposição
lista_gpExposicoes = ['GP A', 'GP B', 'GP C', 'GP D', 'dqidgwqudqwd']
valor_optmenu_gpExposicao = tk.StringVar(window) 
valor_optmenu_gpExposicao.set("Selecione uma Opção:") 
optmenu_gpExposicao = tk.OptionMenu(frm_gpExpo, valor_optmenu_gpExposicao, *lista_gpExposicoes) 
optmenu_gpExposicao.grid(row=1, column=4,sticky='e')

#frame para as inst
frm_inst = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_inst.grid(row=1,column=6,columnspan=2,pady=20,sticky='e',padx=40)

#rótulo da instituição
lbl_instituicao = tk.Label(master=frm_inst, text='Instituição:', font=('Arial', 16))
lbl_instituicao.grid(row=1, column=6,sticky='w')

#Menu com as instituições
lista_instituicoes = ['Inst A', 'Inst B', 'Inst C', 'Inst D', 'dwqdqdwqdqd']
valor_optmenu_instituicao = tk.StringVar(window) 
valor_optmenu_instituicao.set("Selecione uma Opção:") 
optmenu_instituicao = tk.OptionMenu(frm_inst, valor_optmenu_instituicao, *lista_instituicoes) 
optmenu_instituicao.grid(row=1, column=7,sticky='e')

window.mainloop()
