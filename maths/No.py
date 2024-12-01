#3099. Harshad Number


def isHarshad( x):
    y = x
    sum = 0
    
    while x > 0:
        
        z = x % 10
        sum = sum + z
        x = x // 10
    
    if  y % sum ==0:
        return sum
    else:
        return -1

x = 23
print(isHarshad(x))