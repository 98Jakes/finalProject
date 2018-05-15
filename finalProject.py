import string
def randomNumAssignment(numLetter):
    lowerCase = string.ascii_lowercase
    print(lowerCase[numLetter])
def main():
    for x in range(0, 26):
        randomNumAssignment(x)
    
main()