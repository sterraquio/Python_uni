"""
autor:Luis anaguano,Javier Ortiz,Adrick Buitrago
2260323,2360134,2360219
fecha:18/4/2023
"""


#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================

# Proposito:hacer una condicion anidada simple para que le envie a la funsion principlal para saber si es aceptado o rechazado
# Contrato:condicion(entero,real,entero,entero,entero,entero,entero,entero)
# Ejemplo:condicion(edad,altura,peso,20,26,65,75,185)//devuelve:"rechazado"
# Encabezado
# Cuerpo

def condicion(e,a,p,años1,años2,peso1,peso2,altur):
    devuelve="rechazado(a)"
    if e >= años1 and e <= años2: 
        print("flag")
        if a>=altur:
            print("flag")
            if p>=peso1 and p<=peso2:
                print("flag")
                devuelve="aceptado(a)"
    return devuelve

#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito:saber si un hombre o una mujer entran a un equipo de voley teniendo unos requisitos
# Contrato:principal(texto,entero,float,texto,entero)
# Ejemplo:principal()->conHoM:"mujer",edad:22,altura:166,nombre:yasmin,peso:62->conda=condicion(edad,altura,peso,20,26,65,75,185)//"señor(a)" yasmin "usted ha sido",rechazado(a)
# Encabezado
# Cuerpo
def principal():
    conHoM=input("eres hombre o mujer: ").lower
    edad=int(input("ingrese su edad: "))
    altura=float(input("ingrese su altura: "))
    nombre=input("ingrese su nombre: ")
    peso=int(input("ingrese su peso: "))
    if conHoM == "mujer":
        condA=condicion(edad,altura,peso,20,26,65,75,185)
    else :
        condA=condicion(edad,altura,peso,23,29,88,98,192)
    print ("señor(a)",nombre,"usted ha sido",condA)
#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()
