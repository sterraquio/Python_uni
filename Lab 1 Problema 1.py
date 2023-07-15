'''
Fundamentos de Programación Imperativa
Nombre y código del autor: Andrick Buitrago Piedrahita 2360219
Fecha de realización: 3 de abril del 2023

'''




#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito: Es pedir 3 números enteros al usuario y mostrar los datos digitados por el usuario y también esos mismos 3 números enteros rotados a la derecha.
# Contrato: De datos de entrada son 3 números enteros y de salida son los números digitados por el usuario y también esos mismos 3 números enteros rotados a la derecha.
# Ejemplo: Para los números 8, 5, 1. Rotados a la derecha deberá ser 1, 5, 8
# Encabezado: principal
def principal():
    entero1 = int(input("Ingrese el primer número entero: "))
    entero2 = int(input("Ingrese el segundo número entero: "))
    entero3 = int(input("ingrese el tercer número entero: "))
    print("Los números digitados son:",
      "Primero:",str(entero1),
      "segundo:",str(entero2),
      "tercero:",str(entero3))
    control = entero1
    entero1 = entero3
    entero3 = entero2
    entero2 = control
    print("Los 3 números digitados rotados a la derecha,",
      "Primero:",str(entero1),
      "segundo:",str(entero2),
      "tercero:",str(entero3))

#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()
