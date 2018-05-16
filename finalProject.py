import string
import random
#====================================================================
def cut5 (thatstring):
    newstring = ""
    restofstring = ""
    for i in range (0, 5):
        newstring = newstring + str(thatstring[i])
    for x in range (5, len(thatstring)):
        restofstring = restofstring + str(thatstring[x])
    return newstring

def take5 (thatstring):
    restofstring = ""
    for x in range (5, len(thatstring)):
        restofstring = restofstring + str(thatstring[x])
    return restofstring
    
def fillArray (instring):
    newstring = instring
    while (len(newstring) > 0):
        ariel = [0]*(len(newstring)//5)
        for x in range(0, (len(newstring)//5)):
            ariel[x] = cut5(newstring)
            newstring = take5(newstring)
    print(ariel)
#====================================================================


# function generates array of random numbers, turns them into integers, and assigns them to letter of alphabet
def generateRandomNumber(index):
    numLetterArray = [0] * 26
    for x in range(0, 26):
        encryptionArray = [0] * 5
        for i in range(0, 5):
            encryptionArray[i] = random.randint(0,9)
            numLetterArray[x] = encryptionArray
        
    return numLetterArray[index]
     
def generateForEachLetter(userString):
    lowerCase = string.ascii_lowercase
    userStringLen = len(userString)
     
    encryptedData = [0] * userStringLen
 
    for i in range (0, userStringLen):
        for x in range(0, 26):
            if(lowerCase[x] == userString[i]):
                encryptedData[i] = generateRandomNumber(x)
     
    return encryptedData
    
def output():
    userSeed = int(input("Please enter a seed number, an integer. "))
    random.seed(userSeed)
     
    userString = str(input("What is the message you want to encrypt? "))
    encryptedData = generateForEachLetter(userString)
    
    encryptedString = ''.join(str(e) for e in encryptedData)
     
    with open('output.txt', 'w') as output:
        output.write(encryptedString)
    
def createListOfInts(newFile):
    newVal = ""
    justIntegers = ""
    
    m = 0
    a = [0] * len(newFile)
    for x in newFile:
        a[m] = list(x)
        m = m + 1
    
    for x in range(0, len(newFile)):
        if(a[x] == ['0'] or a[x] == ['1'] or a[x] == ['2'] or a[x] == ['3'] or a[x] == ['4'] or a[x] == ['5'] or a[x] == ['6'] or a[x] == ['7'] or a[x] == ['8'] or a[x] == ['9']):
            newVal = newVal + str(a[x])
    
    for i in range(0, len(newVal)):
        if(newVal[i] == '0' or newVal[i] == '1' or newVal[i] == '2' or newVal[i] == '3' or newVal[i] == '4' or newVal[i] == '5' or newVal[i] == '6' or newVal[i] == '7' or newVal[i] == '8' or newVal[i] == '9'):
            justIntegers = justIntegers + newVal[i]
            
    return justIntegers

def new5(a):
    newString = ""
    for x in range(0,5):
        newString = newString + a[x]
        
    return newString
    
    
    
def readFile():
    file = open("output.txt", "r")
    lines = str(file.readlines())
    file.close()
    
    integerList = createListOfInts(lines)
    
    arrayLength = int(len(integerList) / 5)
    
    b = [0] * arrayLength
    a = [0] * 5
    
    newVal = new5(integerList)
    
    print(newVal)
    
    for x in range(0,5):
        a[x] = int(newVal[x])
        
    print(a)
        
    
            
    
def main():
    output()
    readFile()
     
main()