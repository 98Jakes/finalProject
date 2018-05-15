
import string
import random

# function generates array of random numbers, turns them into integers, and assigns them to letter of alphabet
def generateRandomNumber():
    a = [0] * 26
    
    for x in range(0, 26):
        b = [0] * 5
        for i in range(0, 5):
            b[i] = random.randint(0,9)
            a[x] = b
        
    print(a[b[i]])
    
def randomNumAssignment():
    lowerCase = string.ascii_lowercase
    generateRandomNumber()
    
def main():
    userSeed = int(input("Please enter a seed number, an integer."))
    random.seed(userSeed)
    
    userString = str(input("Please enter the message you want to encrypt."))
    
    randomNumAssignment()
    
main()

