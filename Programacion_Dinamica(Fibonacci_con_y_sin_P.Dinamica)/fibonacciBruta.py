#FIBONACCI //N = 5 -> +5 -> n = 60///

#Sin P.Dinamica N = 10 - N = 50
def fibonacci(n): 
    if n <= 1: 
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(fibonacci(n))