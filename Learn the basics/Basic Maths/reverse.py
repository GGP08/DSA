def reverse(n):
    rev = 0
    while n > 0:
            digit = n % 10
            n = n // 10
            rev = rev * 10 + digit
    return rev

if __name__ == "__main__":
      n = int(input("Enter a number: "))
      print(f"The reverse of {n} is:", reverse(n))