import string
import random
isVar = int(input("What is var"))
def cut5 (isVar,thatstring):
    newstring = ""
    restofstring = ""
    for x in range (0, 5):
        newstring = newstring + str(thatstring[x])
    for x in range (5, len(thatstring)):
        restofstring = restofstring + str(thatstring[x])
    if isVar == 1 :
        return newstring
    elif isVar == 0 :
        return restofstring
        
        
    


stringnum = "123151249128471513525"
##array = [0] * len(stringnum)
##nuew = ""
##for i in range (0, len(stringnum)):
##    array[i] = int(stringnum[i])
##newstr = ""
##for x in range (0, len(stringnum)):
##    for i in range (0, 5):
##        if string.digits[i] == stringnum[x] :
##            newstr = newstr + str(array[x])
##for b in range (0,len(stringnum)):
##    for u in range (b, b+5):
##        nuew = nuew + str(newstr[u])

            
##print (newstr)
##print (array)
isVar
print (cut5(isVar, stringnum))
