def factorial(n):
    fac = 1
    for idx in range(2, n+1):
        fac = fac * idx
    return fac


def factorial2(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


if __name__ == "__main__":
    print(factorial(10))
    print(factorial2(10))