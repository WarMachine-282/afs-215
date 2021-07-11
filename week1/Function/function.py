def perfectNumber(n):
    sum = 0 
    for s in range(1, n):
        if n % s == 0:
            sum += s
    return sum == n 
print(perfectNumber(28))

