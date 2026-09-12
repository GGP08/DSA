def pattern20(n):

    spaces = 2 * n -2
    for i in range(1, (2*n-1)+1):
        stars = i
        if i > n:
            stars = 2*n - i

        #stars
        for j in range(1, stars+1):
            print("*", end = " ")

        #spaces
        for j in range(1, spaces+1):
            print(" ", end = " ")

        #stars
        for j in range(1, stars+1):
            print("*", end = " ")

        if i < n:
            spaces -= 2
        else:
            spaces += 2
        print()


if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern20(n)