n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

#precompute
mpp = {}
for i in range(n):
    if arr[i] in mpp:
        mpp[arr[i]] += 1
    else:
        mpp[arr[i]] = 1

#queries
q = int(input())
for i in range(q):
    number = int(input())

    #fetch
    print(mpp[number])