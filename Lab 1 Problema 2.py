'''
Fundamentos de Programación Imperativa
Nombre y código del autor: Andrick Buitrago Piedrahita 2360219
Fecha de realización: 6 de abril de 2023

'''

#==============================================
#            FUNCIÓN AUXILIAR 1
#==============================================
'''
Por cada función auxiliar y según el diseño realizado transcriba.
'''

# Proposito: Calcular la masa de una persona a partir de dividir pesoT entre 9.8
# Contrato: De entrada, el peso de la persona y de salida la masa de la persona a partir de la división de pesoT entre 9.8
# Encabezado: calcular_masa
# Ejemplo 1: Una persona ingresa el peso de 62, entonces como resultado sería 6.326530612244897
# Ejemplo 2: Una persona ingresa el peso de 70, entonces como resultado será 7.142857142857142
# Cuerpo:
def calcular_masa(pesoT:float)->float:
    masa=pesoT/9.8
    return masa


#==============================================
#            FUNCIÓN AUXILIAR 2
#==============================================
'''
Por cada función auxiliar y según el diseño realizado transcriba.
'''

# Proposito: Calcular el peso de una persona en los diferentes cuerpos celestes, multiplicando la masa por la gravedad del cuerpo celeste.
# Contrato: De entrada, es la masa y de salida es el peso en los diferentes cuerpos celestes.
# Encabezado: calcular_peso
# Ejemplo 1: En caso de que la masa sea 6.326530612244897, el peso en marte aproximadamente es  23.478, en jupiter aproximadamente es 156.835, en la luna aproximadamente es 10.262.
# Ejemplo 2: En caso de que la masa sea 7.142857142857142, el peso en marte aproximadamente es 26.507, en jupiter aproximadamente es 177.071, en la luna aproximadamente es 11.586.
# Cuerpo:
def calcular_peso(masa:float, celeste:float)->float:
    peso=masa*celeste
    return peso


#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito: Interactuar con el usuario pidiéndole el peso de una persona, para luego invocar las dos funciones auxiliares que harán el cálculo para mostrarle el peso en los diferentes cuerpos celestes.
# Contrato: De entrada, es el peso de una persona y mostrando el peso de una persona en los diferentes cuerpos celestes.
# Ejemplo 1: En caso de que una persona ingrese el peso de 62 se mostrará el peso en los siguientes cuerpos celestes: el peso en marte aproximadamente es  23.478 KG, en jupiter aproximadamente es 156.835 KG, en la luna aproximadamente es 10.262 KG.
# Ejemplo 2: En caso de que una persona ingrese el peso de 70 se mostrará el peso en los siguientes cuerpos celestes: el peso en marte aproximadamente es 26.507 KG, en jupiter aproximadamente es 177.071 KG, en la luna aproximadamente es 11.586 KG.
# Encabezado: principal
# Cuerpo:
def principal():
    pesoT=float(input("Ingrese el peso de la persona que quiere saber su peso en diferentes cuerpos celestes: "))
    marteG=3.711
    jupiterG=24.79
    lunaG=1.622
    masa=calcular_masa(pesoT)
    pesoMarte=calcular_peso(masa,marteG)
    pesoJupiter=calcular_peso(masa,jupiterG)
    pesoLuna=calcular_peso(masa,lunaG)    
    print("El peso en marte es:",round(pesoMarte, 3),"KG")
    print("El peso en júpiter es:",round(pesoJupiter, 3),"KG")
    print("El peso en la luna es:",round(pesoLuna, 3),"KG")
    
            

#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()

