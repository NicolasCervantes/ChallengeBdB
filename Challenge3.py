# coding=utf-8

# MD5 Hash f0c9fa661a29e609aceec5d02f521b89

def minChange(coins):
    coins.sort() # ordenar el arreglo de menor a mayor
    count = 1 # contador que llevara el valor a retornar
    foundChange = True
    while foundChange: # mientras que se siga encontrando cambio se busca en la lista
        for i in coins:
            if (i <= count): # si el número es menor o igual al contador, significa que se puede generar cambio a partir de esos números de la lista
                count = count + i
            else: # si el número es mayor, significa que ya se han usado todos los números de la lista para crear las sumas
                foundChange = False # se entiende entonces que al no haber más números, se encuentra el cambio mínimo
    return count

testList = [5,7,1,1,2,3,22]
print minChange(testList)