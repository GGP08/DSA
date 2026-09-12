def pattern12(n):
    space = 2 * (n - 1)

    for i in range(1, n + 1):

        # numbers increasing
        for j in range(1, i + 1):
            print(j, end="")

        # spaces
        for j in range(space):
            print(" ", end="")

        # numbers decreasing
        for j in range(i, 0, -1):
            print(j, end="")

        print()

        space -= 2


if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern12(n)