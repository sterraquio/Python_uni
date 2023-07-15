def generar (d):
    s = ""
    i = len(d)-1
    while(i>=0):
        s = s + d[i]+ " "
        i = i -1
    return s

def filtrar(letra, d):
    s = ""
    i = 0
    while(i < len(d)):
        p = d[i]
        while (p==letra):
            s=s + d[i] + " "
    i += 1
    return s

def principal ():
    datos = ["Luz", "Juan", "Veronica", "Nathalie", "Victor"]
    resultado1 = generar(datos)
    resultado2 = filtrar("V", datos)
    print(resultado1, "\n", resultado2)

principal()