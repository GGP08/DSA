#parameterized way
"""def sum(i, res):
    if i < 1:
        print(res)
        return
    sum(i-1, res+i)


if __name__ == "__main__":
    n = int(input())
    sum(n, 0)"""


#functional
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

if __name__ == "__main__":
    n = int(input())
    print(sum(n))