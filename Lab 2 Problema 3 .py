"""autores:Luis anaguano,Javier Ortiz,Adrick Buitrago
2260323,2360134,2360219
fecha:18/4/2023"""
from time import localtime

#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
# Proposito:convertir el nombre de un mes en su correspondiente numero,usando una estructura
#          condicional que verifica cada posible nombre de mes y devuelve su numero correspondiente.
# Contrato:sacarNumes(texto)---->entero
# Ejemplo:si se llama a sacarNumes("mayo"),la funcion devolvera 5
# Encabezado:sacarNumes(mes):
# Cuerpo

def sacarNumes(mes):
    if mes=="enero":
        devuelve=1
    elif mes=="febrero":
        devuelve=2
    elif mes=="marzo":
        devuelve=3
    elif mes=="abril":
        devuelve=4
    elif mes=="mayo":
        devuelve=5
    elif mes=="junio":
        devuelve=6
    elif mes=="julio":
        devuelve=7
    elif mes=="agosto":
        devuelve=8
    elif mes=="septiembre":
        devuelve=9
    elif mes=="octubre":
        devuelve=10
    elif mes=="noviembre":
        devuelve=11
    elif mes=="diciembre":
        devuelve=12
    return  devuelve

#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
# Proposito:calcula la diferencia entre dos numeros y devuelve el valor absoluto de esta diferencia.
# Contrato:result(entero,entero)----->entero
# Ejemplo:queremos calcular la diferencia entre 10 y 5 para hacerlo llamamos a la funcion(result) y esta devuelve el valor
#         absoluto de la diferencia,que en este caso es 5 por lo tanto el resultado seria 5
# Encabezado:def result(n,n2):
# Cuerpo
def result(n,n2):
    devuelve=n2-n
    if devuelve<0:
        devuelve*=(-1)
    return devuelve
#==============================================
#            FUNCIÓNES AUXILIARES
#==============================================
# Proposito:compara dos valores numericos enteros y devuelve true si el valor es mayor o igual  que el numero entero o false en caso contrario.
# Contrato:revisionCum(entero,entero)------>booleano
# Ejemplo:digamos que cumplimos años en marzo este mes se convierte en su valor numerico correspondiente el cual es (3) y se compara con el mes
#          actual(abril) lo que nos dice la funcion es 3 es mayor o igual a 4 dandonos false haciendo que no reste 1
# Encabezado:def revisionCum(mos,n):
# Cuerpo
def revisionCum(mos,n):
    return mos>=n

#==============================================
#           FUNCIÓN PRINCIPAL
#==============================================
# Proposito:es pedir al usuario su fecha de nacimiento y obtener su edad actual tambien calcula la edad actual del usuario en años,meses,dias.
# Contrato:pricipal(entero,texto,entero)------>entero,entero,entero
# Ejemplo:si se llama a la funcion principal() y se ingresan los siguientes valores,dia de nacimiento:13,mes de nacimiento:febrero,año de nacimiento:1990
#         la funcion calculara y mostrara en pantalla que el usuario tiene 33 años sus meses son 2 y sus dias son 9 en la tierra.

# Encabezado:def principal():
# Cuerpo

def principal():
    diasCum = int(input("ingrese el dia en que nacio: "))
    mesCum = input("ingrese el mes en que nacio: ")
    anioCum = int(input("ingrese el año en que nacio: "))

    t=localtime()
    dia=t.tm_mday
    mes=t.tm_mon
    anio=t.tm_year

    numes = sacarNumes(mesCum)
    mosAnio = result(anioCum,anio)
    mosMes = result(numes,mes)
    mosDia = result(diasCum,dia)
    condi=revisionCum(numes,mes)
    condi2=revisionCum(dia,diasCum)
    if condi==True and condi2==True:
        mosAnio-=1
        
    print("sus años son:",mosAnio,",sus meses son:",mosMes,"y sus dias son:",mosDia,"en la tierra;)")
#==============================================
#           LLAMADO A LA FUNCIÓN PRINCIPAL
#==============================================
principal()
