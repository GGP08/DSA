def palindrome(n):
    n1 = n
    rev  = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        rev = rev * 10 + digit
    if rev == n1:
        return "Palindrome"
    else:
        return "Not Palindrome"

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"{n} is", palindrome(n))