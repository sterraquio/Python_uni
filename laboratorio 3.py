"""autores:Luis anaguano,Javier Ortiz,Adrick Buitrago
2260323,2360134,2360219
fecha:27/4/2023"""


#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
# Proposito:toma tres argumentos numéricos `n`, `n1` y `n2`. La función devuelve un valor entero que indica la relación entre los tres números.
#           El propósito de esta función es verificar si los números son iguales o si hay algún par de números iguales.
# Contrato:condicional(n: entero, n1: entero, n2: entero) -> entero
# Ejemplo:En este ejemplo, la función `condicional` se llama con los argumentos `n=3`, `n1=5` y `n2=3`. Como `n` y `n2` son iguales, la función devuelve 1,
#         que se almacena en la variable `resultado`. Luego, se imprime el valor de `resultado`, que es 1.
# Encabezado:def condicional(n,n1,n2):
# Cuerpo:
import random
def condicional(n,n1,n2):
    devuelve=2
    if n==n1 and n==n2 and n1==n2:
        devuelve=0
    elif n==n1 or n1==n2 or n2==n or n==n1 or n1==n2 or n==n2:
        devuelve =1
    return devuelve
#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
# Proposito:La función auxiliar `saberres()` devuelve un valor numérico dependiendo del valor de entrada `condi`. Si `condi` es igual a cero
#          devuelve el valor 4. Si `condi` es igual a uno, devuelve el valor 1. En cualquier otro caso, devuelve el valor -1.
# Contrato:saberres(entero)----->entero
# Ejemplo:La función evalúa que el valor del parámetro es igual a cero, por lo cual devuelve el número 4.
# Encabezado:def saberres(condi):
# Cuerpo
def saberres(condi):
    if condi == 0:
        return 4
    elif condi == 1:
        return 1
    else:
        return -1
#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito:Es un juego de azar en el que el usuario, al iniciar el juego, indica la cantidad de monedas con las que va a jugar.
#          En cada jugada, se le descuenta una moneda de su saldo y se muestran tres números al azar del 1 al 6. Si los tres números son distintos, no gana nada.
#         Si salen dos números iguales, gana una moneda  moneda.
#         Si salen tres números iguales, gana cuatro monedas. El juego continúa hasta que el jugador se queda sin monedas o decide salir.
# Contrato:principal(entero)------>entero,entero,entero
# Ejemplo:En el ejemplo proporcionado por el programa, el jugador decidió empezar con una sola moneda. En su primera jugada, los números que salieron fueron 4, 2, 2, indicando que había dos números iguales.
#        En consecuencia, el jugador ganó dos monedas, obteniendo un saldo actual de 2. En la siguiente jugada, los números que salieron fueron 4, 6, 3, ninguno de ellos repetido, por lo que el jugador no obtuvo ganancias. No obstante, su saldo actual aumentó a 1. 
#        A pesar de haber obtenido una ganancia en la segunda jugada, el jugador decidió seguir jugando y, en su tercera jugada, obtuvo los números 5, 4, 1, ninguno de ellos repetitivo.
#       Sin embargo, al no haber ganado ninguna moneda en esta ronda, su saldo actual disminuyó a 0. El programa continuó con su función de juego,
#       pero como el jugador ya no tenía monedas,el saldo actual se mostró como -1 y las monedas ganadas o perdidas como -1.
# Encabezado:def principal():
# Cuerpo

def principal():
    money = int(input("Ingrese con cuántas monedas quiere comenzar: "))
    while money <= 0:
        money = int(input("Ingrese con cuántas monedas quiere comenzar: "))

    muestra = 0
    saldo_actual = money
    seguir = True
    while seguir and saldo_actual > 0:
        numbeRandom1 = random.randint(1, 6)
        numbeRandom2 = random.randint(1, 6)
        numbeRandom3 = random.randint(1, 6)
        print("Los números que salieron son:", numbeRandom1, numbeRandom2, numbeRandom3)
        condi = condicional(numbeRandom1, numbeRandom2, numbeRandom3)
        rres = saberres(condi)
        saldo=money
        money -= 1
        muestra += rres
        saldo_actual += rres
        if condi == 0:
            print("TODOS LOS NÚMEROS SON IGUALES. ¡GANASTE +5 MONEDAS!")
        elif condi == 1:
            print("HAY DOS NÚMEROS IGUALES. ¡GANASTE +2 MONEDAS!")
        else:
            print("NINGÚN NÚMERO ES IGUAL. INTENTA DE NUEVO.")
        print("Su saldo antes de jugar fue", saldo, "y su saldo actual es",  saldo_actual)

        if saldo_actual > 0:
            continuar = input("¿Desea seguir jugando? (si/no): ")
            if continuar.lower() != "si":
                seguir = False

    if money<0:
        money*=0
    print("Sus monedas son:", money, "\nSus monedas ganadas o perdidas son:", muestra)
#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()
