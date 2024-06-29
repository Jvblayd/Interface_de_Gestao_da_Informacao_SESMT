from datetime import date
import tkinter as tk
from tkinter import ttk

#Configuração da janela
window = tk.Tk()
window.title('Inventário de Riscos - SESMT')
#window.state('zoomed')
#window_height = window.winfo_screenheight()
#window_width = window.winfo_screenwidth()
#center_x = int(window_width/16)
#center_y = int(window_height/16)
#window.geometry(f'{str(window_width)}x{str(window_height)}+{center_x}+{center_y}')
#window.geometry(f'1200x600+{center_x}+{center_y}')
window.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)

#Data do Dia
data = date.today().strftime('%d/%m/%Y')
lbl_data = tk.Label(master=window, text=f'Data: {data}', font=('Arial', 10))
lbl_data.grid(row=0,column=0,sticky='w',padx=10)

#Head
lbl_head = tk.Label(master=window, text='Inventário de Riscos - SESMT', font=('Arial', 23))
lbl_head.grid(row=1,column=0,sticky='n',columnspan=8)

#frame para as secs
frm_row1 = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_row1.grid(row=2,column=0,columnspan=8,pady=20,sticky='n')

#rótulo da secretaria
lbl_secretaria = tk.Label(master=frm_row1, text='Secretaria:', font=('Arial', 16))
lbl_secretaria.grid(row=2, column=0,sticky='w',padx=10)

#Menu com as secretarias
lista_secretarias = ['Selecione uma Opção:', 'Sec A', 'Sec B', 'Sec C', 'Sec D', 'Secretaria F'] #Trocar por arquivo local
valor_optmenu_secretaria = tk.StringVar(window) 
optmenu_secretaria = ttk.OptionMenu(frm_row1, valor_optmenu_secretaria, *lista_secretarias) 
optmenu_secretaria.grid(row=2, column=1,sticky='w',padx=10)

#rótulo grupo de exposição
lbl_gpExposicao = tk.Label(master=frm_row1, text='Grupo de Exposição:', font=('Arial', 16))
lbl_gpExposicao.grid(row=2, column=2,sticky='w',padx=10)

#Menu com Grupos de exposição
lista_gpExposicoes = ['Selecione uma Opção:', 'GP A', 'GP B', 'GP C', 'GP D', 'dqidgwqudqwd'] #Trocar por arquivo local
valor_optmenu_gpExposicao = tk.StringVar(window) 
optmenu_gpExposicao = ttk.OptionMenu(frm_row1, valor_optmenu_gpExposicao, *lista_gpExposicoes) 
optmenu_gpExposicao.grid(row=2, column=4,sticky='w',padx=10)

#rótulo da instituição
lbl_instituicao = tk.Label(master=frm_row1, text='Instituição:', font=('Arial', 16))
lbl_instituicao.grid(row=2, column=6,sticky='w',padx=10)

#Menu com as instituições
lista_instituicoes = ['Selecione uma Opção:', 'Inst A', 'Inst B', 'Inst C', 'Inst D', 'dwqdqdwqdqd'] #Trocar por arquivo local
valor_optmenu_instituicao = tk.StringVar(window) 
optmenu_instituicao = ttk.OptionMenu(frm_row1, valor_optmenu_instituicao, *lista_instituicoes) 
optmenu_instituicao.grid(row=2, column=7,sticky='w',padx=10)

#frame para os riscos
frm_risk = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_risk.grid(row=3,column=0,columnspan=8,pady=20,sticky='n')

#rótulo dos riscos
lbl_tipo_risk = tk.Label(master=frm_risk, text='Tipo de Risco:', font=('Arial', 11))
lbl_tipo_risk.grid(row=3, column=0,sticky='w',padx=10)

#Menu com os riscos
lista_tipo_risks = ['Selecione uma Opção:', 'Físico', 'Químico', 'Biológico', 'Ergonômico', 'Acidental'] #Trocar por arquivo local
valor_optmenu_tipo_risk = tk.StringVar(window) 
optmenu_tipo_risk = ttk.OptionMenu(frm_risk, valor_optmenu_tipo_risk, *lista_tipo_risks) 
optmenu_tipo_risk.grid(row=3, column=1,sticky='w',padx=10)

#rótulo da descrição dos riscos
lbl_desc_risk = tk.Label(master=frm_risk, text='Descrição do Risco:', font=('Arial', 11))
lbl_desc_risk.grid(row=3, column=2,sticky='w',padx=10)

#Menu com a descrição dos riscos
lista_risks_fisicos = ['Selecione uma Opção:','Fís 1', 'fis 2', 'fis 3'] #Trocar por arquivo local
lista_risks_quimicos = ['Selecione uma Opção:', 'quim 1', 'Quim 2', 'quim 3'] #Trocar por arquivo local
lista_risks_biologicos = ['Selecione uma Opção:', 'bio 1', 'bio 2', 'Bio 3'] #Trocar por arquivo local
lista_risks_ergonomicos = ['Selecione uma Opção:', 'ergo 1', 'ergo 2', 'ergo 3'] #Trocar por arquivo local
lista_risks_acidentais = ['Selecione uma Opção:', 'Ac 1', 'Ac 2', 'Ac 3'] #Trocar por arquivo local
lista_risks_atual = lista_risks_fisicos
valor_optmenu_desc_risk = tk.StringVar(window)  
optmenu_desc_risk = ttk.OptionMenu(frm_risk, valor_optmenu_desc_risk, *lista_risks_atual) 
optmenu_desc_risk.grid(row=3, column=3,sticky='w',padx=10)


#rótulo das fontes
lbl_fonte_risk = tk.Label(master=frm_risk, text='Fonte do Risco:', font=('Arial', 11))
lbl_fonte_risk.grid(row=3, column=4,sticky='w',padx=10)

#Menu com as fontes
lista_fonte_risks = ['Selecione uma Opção:', 'Fonte 1', 'Fonte 2', 'Ft 3', 'Ft 6'] #Trocar por arquivo local
valor_optmenu_fonte_risk = tk.StringVar(window) 
optmenu_fonte_risk = ttk.OptionMenu(frm_risk, valor_optmenu_fonte_risk, *lista_fonte_risks) 
optmenu_fonte_risk.grid(row=3, column=5,sticky='w',padx=10)

#rótulo do nível
lbl_nivel_risk = tk.Label(master=frm_risk, text='Nível do Risco:', font=('Arial', 11))
lbl_nivel_risk.grid(row=3, column=6,sticky='w',padx=10)

#Menu com os níveis
lista_nivel_risks = ['Selecione uma Opção:','Nível 1','Nível 2','Nível 3','Nível 4','Nível 5']#Trocar por arquivo local
valor_optmenu_nivel_risk = tk.StringVar(window)  
optmenu_nivel_risk = ttk.OptionMenu(frm_risk, valor_optmenu_nivel_risk, *lista_nivel_risks) 
optmenu_nivel_risk.grid(row=3, column=7,sticky='n',padx=10)

#frame para as lesões
frm_lesao = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_lesao.grid(row=4,column=0,rowspan=3, pady=20,sticky='n')

#rótulo das lesões/agravos
lbl_lesao = tk.Label(master=frm_lesao, text='Selecione as Lesões/Agravos:', font=('Arial', 13))
lbl_lesao.grid(row=4, column=0,sticky='n',padx=10)

#combobox para as lesões
valores_lesoes = tk.StringVar(window)
combobox_lesoes = ttk.Combobox(master=frm_lesao, state="readonly",textvariable=valores_lesoes)
combobox_lesoes.grid(row=5,column=0,sticky='n',padx=10,pady=10)

#lista múltipla para as lesões
lista_lesoes = ['L1','L2','A1','L3','L6','A2','L7','L8','A3','L9','L10','A6','L11','L12','A7','L13','L16','A8','L17']
listbox_lesoes = tk.Listbox(master=frm_lesao, selectmode="multiple", exportselection=0)
listbox_lesoes.grid(row=6,column=0,sticky='n',padx=10)
for value in lista_lesoes:
   listbox_lesoes.insert(tk.END, value)

# define a function to update the combobox when the user selects or deselects a value
def update_combobox_lesoes():
   # Get selected values from the Listbox widget
   selected_values = [listbox_lesoes.get(idx) for idx in listbox_lesoes.curselection()]
    
   # Update the combobox with the selected values
   #combobox_lesoes.configure(width=40, height=7)
   combobox_lesoes.set(",".join(selected_values))
    
# bind the update_combobox function to the Listbox widget
listbox_lesoes.bind("<<ListboxSelect>>", lambda _: update_combobox_lesoes())

#frame para as medidas
frm_medidas = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_medidas.grid(row=4,column=2,rowspan=3, pady=20,sticky='n')

#rótulo das medidas
lbl_medidas = tk.Label(master=frm_medidas, text='Selecione as Medidas de Controle Existentes:', font=('Arial', 13))
lbl_medidas.grid(row=4, column=2,sticky='n',padx=10)

#combobox para as medidas
valores_medidas = tk.StringVar(window)
combobox_medidas = ttk.Combobox(master=frm_medidas, state="readonly",textvariable=valores_medidas)
combobox_medidas.grid(row=5,column=2,sticky='n',padx=10,pady=10)

#lista múltipla para as medidas
lista_medidas = ['M1','M2','E1','L3','J6','A2','N7','Q8','H3','L9','L10','A6','L11','l12','F7','L13','L16','M8','L17']
listbox_medidas = tk.Listbox(master=frm_medidas, selectmode="multiple", exportselection=0)
listbox_medidas.grid(row=6,column=2,sticky='n',padx=10)
for value in lista_medidas:
   listbox_medidas.insert(tk.END, value)

# define a function to update the combobox when the user selects or deselects a value
def update_combobox_medidas():
   # Get selected values from the Listbox widget
   selected_values = [listbox_medidas.get(idx) for idx in listbox_medidas.curselection()]
    
   # Update the combobox with the selected values
   #combobox_lesoes.configure(width=40, height=7)
   combobox_medidas.set(",".join(selected_values))
    
# bind the update_combobox function to the Listbox widget
listbox_medidas.bind("<<ListboxSelect>>", lambda _: update_combobox_medidas())

#frame para a população exposta
frm_populacao = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_populacao.grid(row=4,column=4,rowspan=3, pady=20,sticky='n')

#rótulo da população exposta
lbl_populacao = tk.Label(master=frm_populacao, text='Selecione as Populações Expostas:', font=('Arial', 13))
lbl_populacao.grid(row=4, column=4,sticky='n',padx=10)

#combobox para as populações expostas
valores_populacao = tk.StringVar(window)
combobox_populacao = ttk.Combobox(master=frm_populacao, state="readonly",textvariable=valores_populacao)
combobox_populacao.grid(row=5,column=4,sticky='n',padx=10,pady=10)

#lista múltipla para as populações expostas
lista_populacao = ['P1','d2','Q1','L3','População','B6','A2','X7','K8','H3','L9','L10','R6','P11','l12','F7','L13','W16','M8','L17']
listbox_populacao = tk.Listbox(master=frm_populacao, selectmode="multiple", exportselection=0)
listbox_populacao.grid(row=6,column=4,sticky='n',padx=10)
for value in lista_populacao:
   listbox_populacao.insert(tk.END, value)

# define a function to update the combobox when the user selects or deselects a value
def update_combobox_populacao():
   # Get selected values from the Listbox widget
   selected_values = [listbox_populacao.get(idx) for idx in listbox_populacao.curselection()]
    
   # Update the combobox with the selected values
   #combobox_lesoes.configure(width=40, height=7)
   combobox_populacao.set(",".join(selected_values))
    
# bind the update_combobox function to the Listbox widget
listbox_populacao.bind("<<ListboxSelect>>", lambda _: update_combobox_populacao())

#evento para mudar as descrições com base no tipo escolhido
ultimo_ajuste = ''
def ajustar_riscos(event):
    global ultimo_ajuste
    if (valor_optmenu_tipo_risk.get() == 'Físico'):
        if not(ultimo_ajuste == 'Físico'):
            optmenu_desc_risk.set_menu(*lista_risks_fisicos)
            ultimo_ajuste = 'Físico'
    
    elif (valor_optmenu_tipo_risk.get() == 'Químico'):
        if not(ultimo_ajuste == 'Químico'):
            optmenu_desc_risk.set_menu(*lista_risks_quimicos)
            ultimo_ajuste = 'Químico'
    
    elif (valor_optmenu_tipo_risk.get() == 'Biológico'):
        if not(ultimo_ajuste == 'Biológico'):
            optmenu_desc_risk.set_menu(*lista_risks_biologicos)
            ultimo_ajuste = 'Biológico'
    
    elif (valor_optmenu_tipo_risk.get() == 'Ergonômico'):
        if not(ultimo_ajuste == 'Ergonômico'):
            optmenu_desc_risk.set_menu(*lista_risks_ergonomicos)
            ultimo_ajuste = 'Ergonômico'
    
    elif (valor_optmenu_tipo_risk.get() == 'Acidental'):
        if not(ultimo_ajuste == 'Acidental'):
            optmenu_desc_risk.set_menu(*lista_risks_acidentais)
            ultimo_ajuste = 'Acidental'

optmenu_desc_risk.bind('<Enter>', ajustar_riscos)

#verificar valores
def leigo():
    print(valores_populacao.get())
    return

bt = ttk.Button(master=window,text='Verificar valores',command=leigo)
bt.grid(row=10,column=0)

window.mainloop()
