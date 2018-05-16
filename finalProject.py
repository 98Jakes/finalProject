import string
import random
 
# function generates array of random numbers, turns them into integers, and assigns them to letter of alphabet
def generateRandomNumber(index):
    numLetterArray = [0] * 26
    for x in range(0, 26):
        encryptionArray = [0] * 5
        for i in range(0, 5):
<<<<<<< HEAD
            b[i] = random.randint(0,9)
        a[x] = b
    print(a)
    print(b)
    
    
def randomNumAssignment(numLetter):
=======
            encryptionArray[i] = random.randint(0,9)
            numLetterArray[x] = encryptionArray
     
    return numLetterArray[index]
     
def generateForEachLetter(userString):
>>>>>>> 580c5fa0ea278a5b1ecf93ac4d385b946a59d0fe
    lowerCase = string.ascii_lowercase
    userStringLen = len(userString)
     
    encryptedData = [0] * userStringLen
 
    for i in range (0, userStringLen):
        for x in range(0, 26):
            if(lowerCase[x] == userString[i]):
                encryptedData[i] = generateRandomNumber(x)
     
    return encryptedData
    
def output():
    userSeed = int(input("Please enter a seed number, an integer."))
    random.seed(userSeed)
     
    userString = str(input("What is the message you want to encrypt?"))
    encryptedData = generateForEachLetter(userString)
     
    encryptedString = ''.join(str(e) for e in encryptedData)
     
    with open('output.txt', 'w') as output:
        output.write(encryptedString)
    

def readFile():
    text_file = open("output.txt", "r")
    lines = text_file.readlines()
    print(lines)

    text_file.close()
    
def main():
    output()
    readFile()
     
main()