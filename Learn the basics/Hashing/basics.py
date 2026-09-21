n = int(input("Enter of array elements"))
arr = []
for i in range(n):
    arr.append(int(input()))

#precomputation
hash = [0] * 13
for i in range(n):
    hash[arr[i]] += 1


#ask queries
q = int(input("Enter no. of queries"))
for i in range(q):
    number = int(input())

    #fetch
    print(hash[number])
