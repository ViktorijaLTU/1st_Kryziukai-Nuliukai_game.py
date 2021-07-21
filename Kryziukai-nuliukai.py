import tkinter as tk

zaidejas1_spalva = "gold"
zaidejas2_spalva = "RoyalBlue4"
teksto_spalva_zaidejas1 = "RoyalBlue4"
teksto_spalva_zaidejas2 = "gold"
informacinio_mygtuko_spalva = "snow"
informacinio_mygtuko_teksto_spalva = "red"
btn_naujas_spalva = "black"
btn_naujas_teksto_spalva = "grey"

def naujas ():
    for x in range(3):
        for y in range(3):
            lentele[x][y].configure(text='',bg="SystemButtonFace")


def laimetojas():
    for x in range(3):
        if lentele[x][0]['text'] == lentele[x][1]['text'] == lentele[x][2]['text'] != '':
            return 1
    for y in range(3):
        if lentele[0][y]['text'] == lentele[1][y]['text'] == lentele[2][y]['text'] != '':
            return 1
    if lentele[0][0]['text'] == lentele[1][1]['text'] == lentele[2][2]['text'] != '':
        return 1
    elif lentele[0][2]['text'] == lentele[1][1]['text'] == lentele[2][0]['text'] != '':
        return 1
    elif tusti_langeliai() == []:
        return 0
    else:
        return -1


def tusti_langeliai():
    e=[]
    for x in range(3):
        for y in range(3):
            if lentele[x][y]['text'] == '':
                e.append((x,y))
    return e


zaidejas = 'X'

def zaidimo_eiga(h,z):
    global zaidejas

    if lentele[h][z]['text'] == '' and laimetojas() == -1:
        if zaidejas == 'X':
            lentele[h][z].configure(text='X',bg = zaidejas1_spalva, fg= teksto_spalva_zaidejas1)
            if laimetojas() == -1:
                zaidejas = 'O'
                btn_info.configure(text=("O eilė"))
            elif laimetojas() == 1:
                btn_info.configure(text=("X LAIMĖJO!!!"))
            elif laimetojas() == 0:
                btn_info.configure(text="LYGIOSIOS. KARTOTI :)")
        elif zaidejas == 'O':
            lentele[h][z].configure(text='O',bg = zaidejas2_spalva, fg= teksto_spalva_zaidejas2)
            if laimetojas() == -1:
                zaidejas = 'X'
                btn_info.configure(text=("X eilė"))
            elif laimetojas() == 1:
                btn_info.configure(text=("O LAIMĖJO!!!"))
            elif laimetojas() == 0:
                btn_info.configure(text="LYGIOSIOS. KARTOTI :)")


programos_ekranas = tk.Tk()
programos_ekranas.title('Kryžiukai-nuliukai_žaidimas')
lentele=[[0,0,0],
         [0,0,0],
         [0,0,0]]

for x in range(3):
    for y in range(3):
        lentele[x][y]=tk.Button(text='',font=('normal',60,'normal'),width=5,height=2,command=lambda row = x,column = y: zaidimo_eiga(row,column))
        lentele[x][y].grid(row=x,column=y)

btn_info=tk.Label(text="X eilė",font=('normal',40,'bold'),bg = informacinio_mygtuko_spalva,fg = informacinio_mygtuko_teksto_spalva)
btn_info.grid(row=3,column=1)
btn_naujas=tk.Button(text='NAUJAS',font=('Courier',18,'bold'),fg=btn_naujas_teksto_spalva,bg = btn_naujas_spalva,command=naujas)
btn_naujas.grid(row=4,column=1)
btn_copyright = tk.Label(text='Created by: ViktorijaLTU, ref. https://github.com/ViktorijaLTU [2021]', bg='wheat2', fg='red3', font=('arial', 10, 'bold'))
btn_copyright.grid(columnspan = 3)
programos_ekranas.mainloop()
