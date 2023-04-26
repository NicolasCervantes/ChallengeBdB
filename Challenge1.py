# coding=utf-8

# MD5 Hash f0c9fa661a29e609aceec5d02f521b89

def switchDigitsFunction(numberList, digit):
    switchList = list()
    for i in reversed(range(len(numberList))): # O(n) pero n <= 100 entonces O(100)
        tempList = numberList[i] # O(1)
        numberWithoutDigit = 0 # O(1)
        lastDigit = 0
        j = 1
        hasToAddNumber = False
        if (tempList == 0):
            switchList.append(numberWithoutDigit)
        while (tempList % 10 != 0 or tempList / 10 != 0): # O(m) m es el número de dígitos que tiene ese número
            lastDigit = tempList % 10
            if (lastDigit < digit):
                hasToAddNumber = True
                numberWithoutDigit = numberWithoutDigit + (lastDigit * j)
                j = j * 10
            tempList = tempList / 10
        if (hasToAddNumber == True):
            switchList.append(numberWithoutDigit)
    return switchList

testList = [813, 903, 0, 999, 83425, 9990, 9909]
print(switchDigitsFunction(testList, 9))
