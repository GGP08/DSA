def name(s, i, n):
    if i > n:
        return
    print(s)
    name(s, i+1, n)

if __name__ == "__main__":
    n = int(input())
    s = "Elsa"
    name(s, 1, n)