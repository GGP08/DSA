def pattern6(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end = " ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern6(n)
