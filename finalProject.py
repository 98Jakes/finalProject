
import string
import random

def generateRandomNumber(numLetter):
    
    
def randomNumAssignment(numLetter, randInt):
    lowerCase = string.ascii_lowercase
    print(lowerCase[numLetter])
    
def main():
    userSeed = int(input("Please enter a seed number, an integer."))
    random.seed(userSeed)
    
    userString = str(input("Please enter the message you want to encrypt."))
    
    for x in range(0, 26):
        randomNumAssignment(x)
    
main()

