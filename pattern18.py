def pattern18(n):
    for i in range(n):

        # starting character
        ch = chr(ord("A") + n - i - 1)

        # characters
        for j in range(i + 1):
            print(ch, end=" ")
            ch = chr(ord(ch) + 1)

        print()


if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    pattern18(n)