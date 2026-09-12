def pattern10(n):
    for i in range(0, 2*n-1):
        stars = i
        if i >= n:
            stars = 2*n-i-2
        for j in range(0, stars+1):
            print("*", end = " ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern10(n)
