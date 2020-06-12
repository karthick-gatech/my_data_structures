#
# Given an input string (s) and a pattern (p),
# implement wildcard pattern matching with support for '?' and '*'.
#
# ? Matches any single character.
# * Matches any sequence of characters (including the empty sequence).
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

dp = {}

def remove_duplicate_stars(p):
    if p == '':
        return p
    p1 = [p[0], ]
    for x in p[1:]:
        if p1[-1] != '*' or p1[-1] == '*' and x != '*':
            p1.append(x)
    return ''.join(p1)


def helper(s, p):
    if (s, p) in dp:
        return dp[(s, p)]

    if p == s or p == '*':
        dp[(s, p)] = True
    elif p == '' or s == '':
        dp[(s, p)] = False
    elif p[0] == s[0] or p[0] == '?':
        dp[(s, p)] = helper(s[1:], p[1:])
    elif p[0] == '*':
        dp[(s, p)] = helper(s, p[1:]) or helper(s[1:], p)
    else:
        dp[(s, p)] = False

    return dp[(s, p)]


def isMatch(self, s, p):
    p = remove_duplicate_stars(p)
    return helper(s, p)