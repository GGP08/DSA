#O(N)

"""def divisors(n):
    for i in range(1, n+1):
        if n%i == 0:
            print(i, end = " ")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    divisors(n) """



#O(sqrt(N))
def divisors(n):
    for i in range(1, int(n ** 0.5)+1):
        if n%i == 0:
            print(i, end = " ")
            if (n//i) != i:
                print(n//i, end = " ")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    divisors(n)
