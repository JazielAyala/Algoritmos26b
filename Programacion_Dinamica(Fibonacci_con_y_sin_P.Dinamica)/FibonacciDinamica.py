#Con P. Dinamica N= 10 - N = 90
def fibonacci_dp(n):
    if n <= 1:
        return n

    F = [0] * (n + 1)

    F[0] = 0
    F[1] = 1

    for i in range (2, n + 1):
        F[i] = F[i - 1] + F[i - 2]

    return F[n]

n = 10
print(fibonacci_dp(n))