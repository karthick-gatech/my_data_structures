res = []
s = "aabbaa"


def find_palindrome(s, plist):
    if len(s) == 0: res.append(plist)
    for i in range(1, len(s) + 1):
        if is_palindrome(s[:i]):
            find_palindrome(s[i:], plist+[s[:i]])


def is_palindrome(s):
    if s == s[::-1]: return True
    else: return False


find_palindrome(s, [])
print res
