def pattern7(n):
    for i in range(n):

        #space
        for j in range(n-i-1):
            print(" ", end = " ")

        #star
        for j in range(2*i+1):
            print("*", end = " ")

        #space
        for j in range(n-i-1):
            print(" ", end = " ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern7(n)
