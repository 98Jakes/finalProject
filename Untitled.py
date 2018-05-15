
import string
import random


    
def main():
    userString = str(input("what is string"))
    lowerCase = string.ascii_lowercase
    userStringLen = len(userString)
    a = [0] * 26
    for x in range(0,26):
        for i in range(0, userStringLen):
            if(lowerCase[x] == userString[i]):
                a[x] = random.randint(0, 9)
    
    print(a)
main()

