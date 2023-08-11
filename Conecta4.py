#4 en raya
import os
import platform
from copy import deepcopy
from colorama import Fore

def inicializa_tablero():
    tablero_vacio=[
            ["-","1","2","3","4","5","6","-"],
            ["-","O","O","O","O","O","O","-"], 
            ["-","O","O","O","O","O","O","-"], 
            ["-","O","O","O","O","O","O","-"],
            ["-","O","O","O","O","O","O","-"],
            ["-","O","O","O","O","O","O","-"],
            ["-","O","O","O","O","O","O","-"],
            ["-","-","-","-","-","-","-","-"]] 
    numero_fichas = 0
    jugadas = deepcopy(jugadas_plantilla)
    return tablero_vacio, numero_fichas, jugadas 

def imprime_tablero(): 
    for i in tablero:
        for j in i:
            print('[',str(j),']',end = " ")
        print()

def limpiar_pantalla():
    if sistema == "Darwin" or sistema == "Linux":
        os.system('clear')
    elif sistema == "Windows":
        os.system("cls")
    
def jugada():
    while True:
        try:
            poner_ficha = int(input("¿En qué casilla desea poner la ficha? "))
            x = jugadas[poner_ficha][0]
            y = jugadas[poner_ficha][1]
            if numero_fichas == 0 or numero_fichas %2 == 0:
                ficha = ficha_roja
            if numero_fichas %2 != 0:
                ficha = ficha_amarilla
            if x >= 1 and x <=7 and y >= 1 and y <= 7:
                return x, y, ficha, poner_ficha
        except:
            print("La coordenada introducida no es válida.")

def meter_ficha(x, y, ficha, numero_fichas, poner_ficha):
    try:
        if tablero[x][y] == "O": 
            tablero[x][y] = ficha
            numero_fichas+=1
            jugadas[poner_ficha][0] = jugadas[poner_ficha][0]-1
            print(jugadas[poner_ficha][0], jugadas[poner_ficha][1])
            return tablero, numero_fichas
        else:
            print("Esa columna está llena, elija una columna vacía.")
            return tablero, numero_fichas
    except:
        print("")

def ganar():
    # Comprobación filas:
    for columna in range(len(tablero)):
        contador_fila = 0
        for fila in range(8):
            if tablero[columna][fila] == ficha:
                contador_fila+=1
            else: 
                contador_fila = 0
            if contador_fila >= 4:
                return True
    # Comprobación columnas:
    for fila in range(len(tablero)):
        contador_columna = 0
        for columna in range(8):
            if tablero[columna][fila] == ficha:
                contador_columna+=1
            else: 
                contador_columna = 0
            if contador_columna >= 4:
                return True
    # Comprobación de las diagonales:
    contador_diagonales=0
    for i in range(len(diagonales)):
        contador_diagonales = 0
        for j in range(len(diagonales[i])):
            print(contador_diagonales)
            x = diagonales[i][j][0]
            y = diagonales[i][j][1]
            if tablero[x][y] == ficha:
                contador_diagonales+=1
            else:
                contador_diagonales = 0
            if contador_diagonales >= 4:
                return True
    # Comprobación de las diagonales en sentido inverso:     
    for i in range(len(diagonales)):
        contador_diagonales = 0
    for j in range(len(diagonales[i])):
        print(contador_diagonales)
        y = diagonales[i][j][0]
        x = diagonales[i][j][1]
        if tablero[x][y] == ficha:
            contador_diagonales+=1
        else:
            contador_diagonales = 0
        if contador_diagonales >= 4:
            return True
                
def empatar():
    if numero_fichas == 36:
        return True
##Main   
# Variables globales necesarias para el desarrollo del juego.   
jugadas =  {1:[6,1],
            2:[6,2],
            3:[6,3],
            4:[6,4],
            5:[6,5],
            6:[6,6]}

                #Diagonal principal
diagonales = {0:[[6,1],[5,2],[4,3],[3,4]],
              1:[[5,2],[4,3],[3,2],[2,5]],
              2:[[4,3],[3,2],[2,5],[1,6]],
                #Diagonales secundarias
              3:[[5,1],[4,2],[3,3],[2,4]],
              4:[[4,2],[3,3],[2,2],[1,5]],
              5:[[4,1],[3,2],[2,3],[1,4]],
              6:[[6,2],[5,3],[4,4],[3,5]],
              7:[[5,3],[4,4],[3,5],[2,6]],
              8:[[6,3],[5,4],[4,5],[3,6]]}

jugadas_plantilla = deepcopy(jugadas)
ficha_roja = Fore.RED+str('0')+Fore.RESET
ficha_amarilla = Fore.YELLOW+str('0')+Fore.RESET
sistema = platform.system()
tablero, numero_fichas, jugadas = inicializa_tablero()

while 1:
    limpiar_pantalla()
    print('Jugadas restantes: ', 36 - numero_fichas)
    if numero_fichas == 0 or numero_fichas %2 ==0:
        print('Turno de las', ficha_roja)
    else:
        print('Turno de las', ficha_amarilla)
    imprime_tablero() 
    x, y, ficha, poner_ficha = jugada()
    tablero, numero_fichas = meter_ficha(x, y, ficha, numero_fichas, poner_ficha)
    if numero_fichas >= 0:
        if ganar():
            limpiar_pantalla()
            imprime_tablero()
            print("¡El jugador de las {} ha ganado la partida!".format(ficha))
            continuar = input('¿Quieres seguir jugando? s/n: ')
            if continuar == 's':
                tablero, numero_fichas, jugadas = inicializa_tablero()
            else:
                print('Partida finalizada con éxito.')
                break
        if empatar():
            limpiar_pantalla()
            imprime_tablero() 
            print("No quedan más fichas por jugar. Empate.")
            continuar = input('¿Quieres seguir jugando? s/n: ')
            if continuar == 's':
                tablero, numero_fichas, jugadas = inicializa_tablero()
            else:
                print('Partida finalizada con éxito.')
                break
        

        