
import string
import random

def generateRandomNumber(numLetter):
<<<<<<< HEAD
    for x in range (0, 26):
    
def randomNumAssignment(numLetter, randInt):
=======
    a = [0] * 26
    b = [0] * 5
    for x in range(0, 26):
        for i in range(0, 5):
            b[i] = random.randint(0,9)
        a[x] = b
    print(a)
    print(b)
    
def randomNumAssignment(numLetter):
>>>>>>> 9b74b890601c982e8349f620f3b38a909f8b5420
    lowerCase = string.ascii_lowercase
    generateRandomNumber(lowerCase[numLetter])
    
def main():
    userSeed = int(input("Please enter a seed number, an integer."))
    random.seed(userSeed)
    
    userString = str(input("Please enter the message you want to encrypt."))
    
    for x in range(0, 26):
        randomNumAssignment(x)
    
main()

