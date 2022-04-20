def calculadoraMes(lista,Nombre):
    persona={}
    tuplaMes=()

    elementosL=lista.split(";")
    cantElemeL=len(elementosL)
    for valores in elementosL:
        ahorro=0
        valorLista=valores.split(";")
        cantElemValor= len(valorLista)
        for posicion in range(cantElemValor):
            if posicion==0:
                mes =valorLista[posicion]
            else:
                ahorro+=int(valorLista[posicion])

        persona["nombre"]=Nombre
        persona["ahorro"]["mes"]= mes 
        persona["ahorro"]["valor"]=ahorro
        print(persona)
