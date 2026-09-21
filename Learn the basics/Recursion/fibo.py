#nth fibonacci number
def fibo(n):
    if n <= 1:
        return n
    last = fibo(n - 1)
    slast = fibo(n - 2)

    return last + slast

if __name__ == "__main__":
    n = 4
    print(fibo(n))