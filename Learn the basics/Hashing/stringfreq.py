s = input()

#pre compute
hash = [0] * 26
for i in range(len(s)):
    hash[ord(s[i]) - ord('a')] += 1

    
q = int(input())
for i in range(q):
    c = input()

    #fetch
    print(hash[ord(c) - ord('a')])