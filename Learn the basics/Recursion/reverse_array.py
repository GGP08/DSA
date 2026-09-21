def reverse(i, a, n):
    if i >= n // 2:
        return
    a[i], a[n - i - 1] = a[n - i - 1], a[i]
    reverse(i + 1, a, n)


if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    reverse(0, a, n)
    print(*a)