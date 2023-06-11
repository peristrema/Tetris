from tkinter import *
import random

root=Tk()
root.title=("TETRIS")
myFrame=Frame(root, width=360, height=720)
myFrame.pack()

caient=[]
caient_l=[]
estatic=[]
estatic_l=[]
tocant=False
fin=False
case=0
altura=0   #posició dins la quadricula
alerta=0
for i in range(24):                          
    caient.append([])
    estatic.append([])
    estatic_l.append([])
    caient_l.append([])
    for j in range(12):
        estatic_l[i].append(Label(myFrame))
        caient_l[i].append(Label(myFrame))
        caient[i].append([j])
        estatic[i].append([j])
for i in range(24):
    for j in range(12):
        caient[i][j]=0
        estatic[i][j]=0
        estatic_l[i][j].config(bg="white")
        estatic_l[i][j].place(x=30*j, y=30*i, width=29, height=29)
        for j in range(12):
            estatic[23][j]=1  

#funcions
######################################################################################################################

def inici():  # deixa caure una peça
    #    while (fin==False):     # mentres no arribi al final o toqui alguna peça
    global altura
    global tocant
    global caient
    global caient_l
    global estatic
    global estatic_l
    global fin
    global case
    altura=0                 # cau una altra peça, posició 0
    tocant=False
    if(fin==False): 
        case = random.randint(0,4)     # comencem triant i creant una peça de les 5 de tetris
        if (case==0):
            caient[0][5]=1
            caient[0][6]=1
            caient[0][7]=1
            caient[0][8]=1
        elif (case==1):
            caient[0][5]=1
            caient[0][6]=1
            caient[0][7]=1
            caient[1][7]=1
        elif (case==2):
            caient[0][5]=1
            caient[0][6]=1
            caient[1][5]=1
            caient[1][6]=1
        elif (case==3):
            caient[0][5]=1
            caient[0][6]=1
            caient[1][4]=1
            caient[1][5]=1
        else:
            caient[0][6]=1

        myFrame.after(10,mov)
           
def mov():
    global altura
    global tocant
    global caient
    global caient_l
    global estatic
    global estatic_l
    global fin
    for i in reversed(range(23)):                  # avança tota una fila
        for j in range(12):
            if (caient[i][j]!=0 and estatic[i+1][j]!=0):     # pot seguir caient mentres no toqui altres peces
                tocant=True                                  # toca, alarma posada
                if (altura==0): fin=True
                break   #si toca una peça nomes començar ja hem acabat surt del bucle
        else:
            continue
        break    
    if (tocant==True):   #si toca l'estructura posem la peça a l'estructura
        for i in reversed(range(23)):
            for j in range(12):          # afegeix peça a l'estructura 
                if (estatic[i][j]==0):   # fins a quatre pisos per si de cas
                    estatic[i][j]=caient[i][j]  
                    caient[i][j]=0       # i esbora la peça que cau pq no la dibuixi després
                if (estatic[i-1][j]==0 and i>=1): 
                    estatic[i-1][j]=caient[i-1][j]  
                    caient[i-1][j]=0
                if (estatic[i-2][j]==0 and i>=2): 
                    estatic[i-2][j]=caient[i-2][j]  
                    caient[i-2][j]=0
                if (estatic[i-3][j]==0 and i>=3): 
                    estatic[i-3][j]=caient[i-3][j]  
                    caient[i-3][j]=0
    else:
        for i in reversed(range(23)):
            for j in range (12):
                caient[i+1][j]=caient[i][j]       #si tot va bé cau a la fila inferior
                if (caient[i][j]!=0): 
                    caient_l[i][j].config(bg="white")
                    caient_l[i][j].place(x=30*j, y=30*i, width=29, height=29)
                    caient[i][j]=0   
    if (fin==False):                            # i s'esborra l'anterior
        for i in range(23):
            for j in range(12):
                if (caient[i][j]!=0):
                    if (case==0):
                        caient_l[i][j].config(bg="yellow")
                        caient_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
                    elif (case==1):
                        caient_l[i][j].config(bg="blue")
                        caient_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
                    elif (case==2):
                        caient_l[i][j].config(bg="red")
                        caient_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
                    elif (case==3):
                        caient_l[i][j].config(bg="green")
                        caient_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
                    else:
                        caient_l[i][j].config(bg="brown")
                        caient_l[i][j].place(x=30*j,y=30*i, width=29, height=29)                                                      
                if (estatic[i][j]!=0):
                    if (case==0):
                        estatic_l[i][j].config(bg="yellow")
                        estatic_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
                    elif (case==1):
                        estatic_l[i][j].config(bg="blue")
                        estatic_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
                    elif (case==2):
                        estatic_l[i][j].config(bg="red")
                        estatic_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
                    elif (case==3):
                        estatic_l[i][j].config(bg="green")
                        estatic_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
                    else:
                        estatic_l[i][j].config(bg="brown")
                        estatic_l[i][j].place(x=30*j,y=30*i, width=29, height=29)
    altura+=1
    print (altura, case, tocant, fin)
    if (tocant==True and fin==False): 
        myFrame.after(10,inici)
    elif(tocant==False and fin==False):
        myFrame.after(10,mov)
    else:
        return

#################################################################

# while (fin==False):
inici()
    # mov()

myFrame.after(10,mov)    
root.mainloop()
