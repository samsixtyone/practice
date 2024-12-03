def fac(n):
    if n == 1:
        return n
    else:
        return (n * fac(n-1))

print("5! =", fac(5))
