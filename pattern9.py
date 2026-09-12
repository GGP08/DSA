def pattern9(n):
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

    for i in range(n):

        #star
        for j in range(i):
            print(" ", end = " ")

        #space
        for j in range(2*n - (2*i+1)):
            print("*", end = " ")

        #star
        for j in range(i):
            print(" ", end = " ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern9(n)

