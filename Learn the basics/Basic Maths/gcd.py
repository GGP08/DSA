#O(min(n1, n2))
"""def gcd(n1, n2):
    for i in range(1, min(n1, n2)+1):
        if n1%i == 0 and n2%i == 0:
            gcd = i
    return gcd

if __name__ == "__main__":
    n1 = int(input("Enter a number1: "))
    n2 = int(input("Enter a number2: "))
    print(gcd(n1, n2)) """

def gcd(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if n1%i == 0 and n2%i == 0:
            print(i)
            break
if __name__ == "__main__":
    n1 = int(input("Enter a number1: "))
    n2 = int(input("Enter a number2: "))
    gcd(n1, n2)