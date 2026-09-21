def palindrome(i, s):
    if i >= n//2:
        return True
    if s[i] != s[n-i-1]:
        return False
    return palindrome(i+1, s)

if __name__ == "__main__":
    s = "MADSM"
    n = len(s)
    print(palindrome(0, s))