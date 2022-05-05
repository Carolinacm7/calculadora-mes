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

        # calculadoraMes(registroDeAhorros,nombre)
# calculadoraMes("Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4" ,"daniel")
# ('daniel', {'Enero': 11, 'Febrero': 7, 'Marzo': 11, 'Abril': 15})
# 

def calculadoraMes(lista, nombre):
    persona = {"nombre": "", "ahorro": {}}
    
    persona["nombre"] = nombre
    elementosL = lista.split(";")
    cantElemeL = len(elementosL)
    
    for valores in elementosL:
        ahorro = 0
        valorLista = valores.split(",")
        cantElemValor = len(valorLista)
        for posicion in range(cantElemValor):
            if posicion == 0:
                mes = valorLista[posicion]
            else :
                ahorro += int(valorLista[posicion])
        
        persona["ahorro"][mes] = ahorro
    tuplaMes = tuple(persona.values())
    
    return tuplaMes

print(calculadoraMes("Enero,4,3,4;Febrero,4,3;Marzo,4,3,4;Abril,4,3,4,4" ,"daniel"))
