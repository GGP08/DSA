def bubble(arr, n):
    for i in range(n-1, -1, -1):
        isdid = 0
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isdid = 1

        if isdid == 0:
            break

    print(*arr)

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    bubble(a, n)