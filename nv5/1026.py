"""
def getBinary(x):
        arr = []
        while x >= 1:
                arr.append(x%2)
                x = x//2
        
        return arr 

def sum(arr1, arr2):
    while len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            arr2.append(0)
        elif len(arr2) > len(arr1):
            arr1.append(0)
    
    result = []
    for i in range(len(arr1)):
        if arr1[i] + arr2[i] == 2:
            result.append(0)
        else:
            result.append(arr1[i] + arr2[i])
    return result


while True:

    try:
        x, y = map(int, input().split())
        b1 = getBinary(x)
        b2 = getBinary(y)
        resultB = sum(b1, b2)
        resultD = 0
        for i in range(len(resultB)):
            resultD += (2**i) * resultB[i]
        print(f'{resultD:.0f}')
    
    except EOFError:
        break
"""

try:
    while True:
        a, b = map(int, input().split())
        print(a ^ b)
except EOFError:
    pass



   

