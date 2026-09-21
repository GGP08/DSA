#1 to N => O(N)
"""def num(i, n):
    if i > n:
        return
    print(i)
    num(i+1, n)

if __name__ == "__main__":
    n = int(input())
    num(1, n)"""

#N to 1 => O(N)
"""def num(i, n):
    if i < 1:
        return
    print(i)
    num(i-1, n)

if __name__ == "__main__":
    n = int(input())
    num(n, n)"""

#to print 1 to N without using i+1, we can also do i-1 but call before print
"""def num(i, n):
    if i < 1:
        return
    num(i-1, n)
    print(i)

if __name__ == "__main__":
    n = int(input())
    num(n, n)"""


def num(i, n):
    if i > n:
        return
    num(i+1, n)
    print(i)

if __name__ == "__main__":
    n = int(input())
    num(1, n)