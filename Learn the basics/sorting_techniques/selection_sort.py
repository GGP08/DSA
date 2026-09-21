def selection(arr, n):
    for i in range(0, n-1):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    print(*arr)

if __name__ == "__main__":
    n = int(input("Enter number of array elements: "))
    a = []
    for i in range(n):
        a.append(int(input()))
    selection(a, n)