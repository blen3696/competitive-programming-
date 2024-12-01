def fizzBuzz( n):
    arr = []
    for r in range(1, n+1):
        if r%3 == 0 and r%5 ==0:
            arr.append("FizzBuzz")
        elif r%3 == 0:
            arr.append("Fizz")
        elif r%5 ==0:
            arr.append("Buzz")
        else:
            arr.append(str(r))
    return arr
n = 5
print(fizzBuzz(n))
