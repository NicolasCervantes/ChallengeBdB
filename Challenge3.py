# coding=utf-8

# MD5 Hash f0c9fa661a29e609aceec5d02f521b89

# ordenar el arreglo de menor a mayor
# contador empieza en 1
# 1. Busco si en toda la lista esta ese mismo número del contador, si está, sumo 1 al contador, reinicio el aux y vuelvo a empezar el ciclo (break)
# 2. Si ese número del contador no está en la lista, busco si la suma del primer número y el segundo es igual al contador
# 3. Si la suma de esos dos números es igual al contador, sumo el contador, reinicio el aux que tiene la suma de esos dos números y vuelvo a iniciar el ciclo
# 4. Si la suma de esos dos números no es igual al contador, tomo el segundo número (aux) y el siguiente para comparar si su suma es igual al contador
# 5. Si la suma de dos números en toda la lista no logra ser igual al contador, se vuelve a iniciar el ciclo y se toman tres números. Se repiten los pasos 3 y 4 ahora con tres números
# 6. Si la suma de tres números en toda la lista no logra ser igual al contador, se vuelve a iniciar el ciclo y se van añadiendo números hasta que se cubran todas las posibles sumas dentro de la lista
# 7. Si el contador no logra ser igualado después de estos pasos, se devuelve ese valor como respuesta

def minChange(coins):
    coins.sort()
    count = 1
    numbQuantity = 1
    foundChange = True
    while foundChange:
        for i in range(0, len(coins)):
            aux = coins[i]
        if (aux == count):
            count = count + 1
            aux = coins[0]
            break
        else:
            for j in range(numbQuantity - i, len(coins)):
              aux = sum(coins[i:j])
              numbQuantity = numbQuantity + 1
            if (aux == count):
                count = count + 1
                aux = coins[0]
                break
    foundChange = False
    return count

testList = [5,7,1,1,2,3,22]
print minChange(testList)