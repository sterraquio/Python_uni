'''
Fundamentos de Programación Imperativa
Nombre y código del autor:
Fecha de realización: 12/05/2023

'''

#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
'''
Por cada función auxiliar y según el diseño realizado transcriba.
'''

# Proposito:
# Contrato:
# Ejemplo:
# Encabezado:
# Cuerpo:
def calcularSalario(categoria):
    salario=0
    if categoria=="A":
        salario=1200000
    elif categoria=="B":
        salario=1750000
    elif categoria=="C":
        salario=3200000
    return salario

        

#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito:
# Contrato: principal()
# Ejemplo:
# Encabezado: principal()
# Cuerpo
def principal():
    print("Las categorías existentes son: A, B y C. Por favor ingrese su categoría")
    zapato=input("Ingrese su Categoría: ").upper()
    mostrar=calcularSalario(zapato)
    print("Su salario es: ", mostrar,"$")
#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()