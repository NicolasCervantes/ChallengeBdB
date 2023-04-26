# coding=utf-8

# MD5 Hash f0c9fa661a29e609aceec5d02f521b89

def squaredOrderedList(ascendingList, rangeDigit):
    squaredList = list()
    for i in range(len(ascendingList)):
        x = pow(ascendingList[i], 2) #se eleva al cuadrado cada elemento de la lista dada
        if (x < rangeDigit):
            squaredList.append(x) #se agrega a la nueva lista
    for i in range(len(squaredList)):
        for j in range(len(squaredList)):
            if squaredList[i] < squaredList[j]: #se comparan las dos posiciones de la lista para ver si el numero siguiente es menor
                aux = squaredList[j] #se usa una variable auxiliar para almacenar el valor mientras se cambia de posición
                squaredList[j] = squaredList[i]
                squaredList[i] = aux
    return squaredList

testList = [-4,-3,-2,1,5,6,7,9,10,12,14]
print (squaredOrderedList(testList,99))