from datetime import date
import tkinter as tk
from tkinter import ttk

#Configuração da janela
window = tk.Tk()
window.title('GI - SESMT')
#window.state('zoomed')
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
lista_secretarias = ['Sec A', 'Sec B', 'Sec C', 'Sec D', 'Secretaria F'] #Trocar por arquivo local
valor_optmenu_secretaria = tk.StringVar(window) 
valor_optmenu_secretaria.set("Selecione uma Opção:") 
optmenu_secretaria = tk.OptionMenu(frm_row1, valor_optmenu_secretaria, *lista_secretarias) 
optmenu_secretaria.grid(row=2, column=1,sticky='w',padx=10)

#frame para os grupos de Expo
#frm_gpExpo = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
#frm_gpExpo.grid(row=1,column=2,columnspan=4,pady=20,sticky='n')

#rótulo grupo de exposição
lbl_gpExposicao = tk.Label(master=frm_row1, text='Grupo de Exposição:', font=('Arial', 16))
lbl_gpExposicao.grid(row=2, column=2,sticky='w',padx=10)

#Menu com Grupos de exposição
lista_gpExposicoes = ['GP A', 'GP B', 'GP C', 'GP D', 'dqidgwqudqwd'] #Trocar por arquivo local
valor_optmenu_gpExposicao = tk.StringVar(window) 
valor_optmenu_gpExposicao.set("Selecione uma Opção:") 
optmenu_gpExposicao = tk.OptionMenu(frm_row1, valor_optmenu_gpExposicao, *lista_gpExposicoes) 
optmenu_gpExposicao.grid(row=2, column=4,sticky='w',padx=10)

#frame para as inst
#frm_inst = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
#frm_inst.grid(row=1,column=6,columnspan=2,pady=20,sticky='e',padx=40)

#rótulo da instituição
lbl_instituicao = tk.Label(master=frm_row1, text='Instituição:', font=('Arial', 16))
lbl_instituicao.grid(row=2, column=6,sticky='w',padx=10)

#Menu com as instituições
lista_instituicoes = ['Inst A', 'Inst B', 'Inst C', 'Inst D', 'dwqdqdwqdqd'] #Trocar por arquivo local
valor_optmenu_instituicao = tk.StringVar(window) 
valor_optmenu_instituicao.set("Selecione uma Opção:") 
optmenu_instituicao = tk.OptionMenu(frm_row1, valor_optmenu_instituicao, *lista_instituicoes) 
optmenu_instituicao.grid(row=2, column=7,sticky='w',padx=10)

#frame para os riscos
frm_risk = tk.Frame(master=window,relief=tk.RAISED,borderwidth=1)
frm_risk.grid(row=3,column=0,columnspan=8,pady=20,sticky='n')

#rótulo dos riscos
lbl_tipo_risk = tk.Label(master=frm_risk, text='Tipo de Risco:', font=('Arial', 16))
lbl_tipo_risk.grid(row=3, column=0,sticky='w',padx=20)

#Menu com os riscos
lista_tipo_risks = ['Físico', 'Químico', 'Biológico', 'Ergonômico', 'Acidental'] #Trocar por arquivo local
valor_optmenu_tipo_risk = tk.StringVar(window) 
valor_optmenu_tipo_risk.set("Selecione uma Opção:") 
optmenu_tipo_risk = tk.OptionMenu(frm_risk, valor_optmenu_tipo_risk, *lista_tipo_risks) 
optmenu_tipo_risk.grid(row=3, column=1,sticky='w')

#rótulo da descrição dos riscos
lbl_desc_risk = tk.Label(master=frm_risk, text='Descrição do Risco:', font=('Arial', 16))
lbl_desc_risk.grid(row=3, column=2,sticky='w',padx=20)

#Menu com a descrição dos riscos
lista_risks_fisicos = ['Fís 1', 'fis 2', 'fis 3'] #Trocar por arquivo local
lista_risks_quimicos = ['quim 1', 'Quim 2', 'quim 3'] #Trocar por arquivo local
lista_risks_biologicos = ['bio 1', 'bio 2', 'Bio 3'] #Trocar por arquivo local
lista_risks_ergonomicos = ['ergo 1', 'ergo 2', 'ergo 3'] #Trocar por arquivo local
lista_risks_acidentais = ['Ac 1', 'Ac 2', 'Ac 3'] #Trocar por arquivo local
lista_risks_atual = lista_risks_fisicos
valor_optmenu_desc_risk = tk.StringVar(window) 
valor_optmenu_desc_risk.set("Selecione uma Opção:") 
optmenu_desc_risk = tk.OptionMenu(frm_risk, valor_optmenu_desc_risk, *lista_risks_atual) 
optmenu_desc_risk.grid(row=3, column=3,sticky='w')


#lista_tipo_risks = ['Físico', 'Químico', 'Biológico', 'Ergonômico', 'Acidental']

#evento para mudar as descrições com base no tipo escolhido
def ajustar_riscos(event):
    match valor_optmenu_tipo_risk.get():
        case 'Físico':
            optmenu_desc_risk['menu'].delete(0, 'end')
            for opt in lista_risks_fisicos:
                optmenu_desc_risk['menu'].add_command(label=opt)
        case 'Químico':
            optmenu_desc_risk['menu'].delete(0, 'end')
            for opt in lista_risks_quimicos:
                optmenu_desc_risk['menu'].add_command(label=opt)
        case 'Biológico':
            optmenu_desc_risk['menu'].delete(0, 'end')
            for opt in lista_risks_biologicos:
                optmenu_desc_risk['menu'].add_command(label=opt)
        case 'Ergonômico':
            optmenu_desc_risk['menu'].delete(0, 'end')
            for opt in lista_risks_ergonomicos:
                optmenu_desc_risk['menu'].add_command(label=opt)
        case 'Acidental':
            optmenu_desc_risk['menu'].delete(0, 'end')
            for opt in lista_risks_acidentais:
                optmenu_desc_risk['menu'].add_command(label=opt)

lbl_desc_risk.bind('<Enter>', ajustar_riscos)
optmenu_desc_risk.bind('<Enter>', ajustar_riscos)
frm_risk.bind('Leave>', ajustar_riscos)

window.mainloop()
