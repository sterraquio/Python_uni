import random
'''
Fundamentos de Programación Imperativa
Nombre y código del autor: Andrick Buitrago Piedrahita 2360219
Fecha de realización: 15/06/2023

'''

#==============================================
#            FUNCIÓNES AUXILIARES 1
#==============================================
'''
Por cada función auxiliar y según el diseño realizado transcriba.
'''

# Proposito: Generar 10 números aleatorios
# Contrato: generadorRandom()->[]int
# Ejemplo: numRandom[4, 5, 8, 12, 20, 9, 17, 5, 10, 9]
# Encabezado: generadorRandom()->[]numRandom
# Cuerpo:
def transformador():
    numRandom = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    control = 0
    while(control<len(numRandom)):
        numRandom[control] = random.randint(0, 20)
        control += 1
    return numRandom

#==============================================
#            FUNCIÓNES AUXILIARES 2
#==============================================
'''
Por cada función auxiliar y según el diseño realizado transcriba.
'''

# Proposito: Calcula cuántos ceros tiene el arreglo.
# Contrato: conteoDeCeros(int)->int
# Ejemplo: aleatorio = [9, 0, 20, 10, 0, 10, 15, 5, 8, 8] Total de ceros: 2
# Encabezado: conteoDeCeros(aleatorio)-> c
# Cuerpo:
def conteoDeCeros(aleatorio):
    control = 0
    c = 0
    while (control< len(aleatorio)):
        if (aleatorio[control]== 0):
            c += 1
        control +=1
    return c
#==============================================
#            FUNCIÓNES AUXILIARES 3
#==============================================
'''
Por cada función auxiliar y según el diseño realizado transcriba.
'''

# Proposito: Calcula cuántos pares hay en los datos del arreglo
# Contrato: conteoDePares([]int)->int
# Ejemplo: aleatorio = [6, 14, 14, 20, 8, 19, 17, 1, 4, 6] Total números de pares del arreglo: 7
# Encabezado: conteoDePares([]arreglo)->conteo
# Cuerpo:
def conteoDePares(arreglo):
    control2=0
    conteo=0
    while(control2< len(arreglo)):
        if(arreglo[control2]%2 == 0):
            conteo +=1
        control2 +=1
    return conteo
#==============================================
#            FUNCIÓNES AUXILIARES 4
#==============================================
'''
Por cada función auxiliar y según el diseño realizado transcriba.
'''

# Proposito: Calcula cuántos impares hay en los datos del arreglo
# Contrato: conteoDeImpares([]int)->int
# Ejemplo: aleatorio = [5, 8, 14, 17, 9, 17, 5, 1, 19, 1] Total de número impares son:  8
# Encabezado: conteoDeImpares([]aleatorio)->conteo
# Cuerpo:
def conteoDeImpares(aleatorio):
    control = 0
    conteo = 0
    while(control < len(aleatorio)):
        if(aleatorio[control]%2 != 0):
            conteo +=1
        control +=1
    return conteo


#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito: Interactuar con el usuario y mostrando el resultado del cálculo de cada subproceso.
# Contrato: principal()
# Ejemplo: aleatorio = [2, 7, 6, 12, 0, 10, 8, 5, 14, 6]
# Total de ceros son: 1
# Total de números pares son:  8
# Total de número impares son:  2

# Encabezado: principal()
# Cuerpo
def principal():
    aleatorio = transformador()
    ceros = conteoDeCeros(aleatorio)
    pares = conteoDePares(aleatorio)
    impares = conteoDeImpares(aleatorio)
    print("Los 10 números aleatorios son: ", aleatorio)
    print("Total de ceros son:", ceros)
    print("Total de números pares son: ", pares)
    print("Total de número impares son: ", impares)


#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()