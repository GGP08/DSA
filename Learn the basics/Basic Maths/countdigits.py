def countdigits(n):
    count = 0
    while n > 0:
        digit = n%10
        n = n//10
        count += 1
    return count

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"The number of digits in {n} is: ", countdigits(n))
