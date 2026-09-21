def prime(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            count += 1
            if n//i != i:
                count += 1
    if count == 2:
        return "Prime"
    else:
        return "Not Prime"

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(prime(n))