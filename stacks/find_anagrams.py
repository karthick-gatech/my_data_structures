from collections import Counter

def findanagrams(s,p):
    res = []
    pcounter = Counter(p)
    scounter = Counter(s[:len(p)-1])
    for i in range(len(p) - 1, len(s)):
        scounter[s[i]] += 1
        if scounter == pcounter:
            print "Found a match"
            res.append(i-len(p)+1)
        scounter[s[i-len(p)+1]] -= 1
        if scounter[s[i-len(p)+1]] == 0:
            del scounter[s[i-len(p)+1]]
    print pcounter
    print scounter
    print res

findanagrams('abab', 'ab')