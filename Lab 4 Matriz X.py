'''
Fundamentos de Programación Imperativa
Nombre y código del autor: Andrick Buitrago Piedrahita - 2360219-2724
Fecha de realización: 16/06/2023

'''

#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
'''
Por cada función auxiliar y según el diseño realizado transcriba.
'''

# Proposito: Suma números dependiendo del número que el usuario ingrese 
# Contrato: sumador([ , ]int)->int
# Ejemplo: Matriz=[[0, 0], [0, 0], [0, 0]] y el usuario ingresa el valor de ‘x’ = 0, el resultado es: [[1, 2], [3, 4], [5, 6]]
# Encabezado: sumado([ , ]matriz)->[ , ]matriz
# Cuerpo:
def sumador(x, matriz):
    control_f = 0
    control_c = 0
    control_G = 1
    while(control_f < len(matriz)):
        while(control_c < len(matriz[0])):
            matriz[control_f][control_c] = x + control_G
            control_c +=1
            control_G +=1
        control_f +=1
        control_c= 0
    return matriz



#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito:Interactuar con el usuario para darle valor a las filas y columnas y dar un valor que el usuario quiera agregar.
# Contrato: principal()
# Ejemplo:El usuario ingresa el número de columnas: 2, el usuario ingresa el número de filas: 3. El usuario ingresa cualquier valor: 0. El programa imprime: [[1, 2], [3, 4], [5, 6]] 
# Encabezado: principal()
# Cuerpo
def principal():
    n = int(input("Ingrese el número de columnas: "))
    m = int(input("Digite el número de filas: "))
    x = int(input("Ingrese un valor cualquiera: "))
    matriz = [[0 for c in range(n)]for f in range (m)]
    matriz = sumador(x, matriz)
    print(matriz)


#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()