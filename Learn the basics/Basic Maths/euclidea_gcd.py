#O(logphi(min(a, b))) => phi = because a and b fluctuates
def euclidean(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a%b
        else:
            b = b%a

    if a == 0:
        return b
    else:
        return a

if __name__ == "__main__":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(euclidean(a, b))