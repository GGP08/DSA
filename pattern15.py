def pattern15(n):
    for i in range(n):
        for j in range(n-i):
            char = chr(65 + j)
            print(char, end = " ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern15(n)
