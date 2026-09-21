def armstrong(n):
    n1 = n
    count = len(str(n))
    res = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        res = res + (digit)**count
    if n1 == res:
        return "armstrong number"
    else:
        return "not an armstrong number"

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"{n} is", armstrong(n))
