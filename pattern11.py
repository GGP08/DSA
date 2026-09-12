def pattern2(n):
    for i in range(n):
        start = 1
        if i % 2 == 0:
            start = 1
        else:
            start = 0
        for j in range(i+1):
            print(start, end = " ")
            start = 1 - start
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern2(n)