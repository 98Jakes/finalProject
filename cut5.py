import string
import random
stringnum = "12315124912847151352"
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



fillArray(stringnum)


array = [0] * len(stringnum)
nuew = ""
for i in range (0, len(stringnum)):
    array[i] = int(stringnum[i])
newstr = ""
for x in range (0, len(stringnum)):
    for i in range (0, 5):
        if string.digits[i] == stringnum[x] :
            newstr = newstr + str(array[x])
##for b in range (0,len(stringnum)):
##    for u in range (b, b+5):
##        nuew = nuew + str(newstr[u])

            
##print (newstr)
##print (array)
##print (cut5(stringnum))
