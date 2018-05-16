import random
import string


integerList = "23232234598239423947"
a = [0] * len(integerList)
num1 = 0
for x in integerList:
    a[num1] = int(x)
    num1 = num1 + 1
            
print(a)

