import random
"""autores:luis anaguano,Andrick buitrago , javier Ortiz 
codigo:2360219,2360134,2260323"""
#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
# Proposito: Recibe un número de 3 dígitos y retorna verdadero si todos los dígitos son diferentes, en caso en que no, retorna falso.
# Contrato: numRandom(entero)->bool
# Ejemplo: numRandom(652)->TRUE
# Encabezado
# Cuerpo
def numRandom(num): 
    digit1 = num//100
    digit2= ((num%100))//10
    digit3=num%10
    res=(digit1 != digit2 and digit1 != digit3 and digit2 != digit3)
    print(digit1,digit2,digit3)
    return res

#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito:se encarga de llamar al modulo "random" que genera un numero aleatorio de 3 digitos y muestra el resultado si es o no diferente a los digitos
# Contrato:principal()->texto
# Ejemplo:principal()->num:123
# Encabezado
# Cuerpo
def principal():
    num= random.randint(100,999)
    print("el numero generado es ",num)
    resulDef=numRandom(num)
    if resulDef==True:
        result="los tres digitos son diferentes"
    else:
        result="los tres digitos no son diferentes"
    print(result)
#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()