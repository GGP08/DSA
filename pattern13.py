def pattern13(n):
    k = 0
    for i in range(n):
        for j in range(i+1):
            print(k+1, end = " ")
            k += 1
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern13(n)