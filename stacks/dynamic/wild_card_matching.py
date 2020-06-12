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
# Dynamic programming approach - D[p_idx][s_idex] which is a match
# between the first p_idx characters of the pattern and the first
# s_idx characters of the string.
#
# ex: *a*b?k = pattern and adcbdk = string.
#     D[p_idx][s_idx] = match between pattern[0...p_idx - 1] and string[0...s_idx - 1]
#
# IF the last characters are the same or pattern character is '?', then
#     D[p_idx][s_idx] = D[p_idx - 1][s_idx - 1]
#    ex: *a*b in *a*b?k matches with adcb in adcbdk because *a* matches adc and b=b
#
# If the pattern character is '*' and there was a match on the previous step i.e D[p_idx-1][s_idx-1]=True then
#
# star at the end of the pattern still results in a match
# star could much as many characters as you wish
#       D[p_idx - 1][i] = True, i >= s_idx-1
#
# So, these are the cases to think -
#  D[p_idx][s_idx] = D[p_idx-1][s_idx-1] if p[p_idx-1] = s[s_idx-1]
#  D[p_idx][i] = True for all i >= s_idx - 1
#    if p[p_idx - 1] = * and D[p_idx-1][s_idx-1] = True
# Algorithm:
#   Start from the table initiated as False everywhere but D[0][0] = True
#   Apply the above roles in a loop and return D[p_len][s_len]
#

class Solution:
    def isMatch(self, s, p):
        s_len = len(s)
        p_len = len(p)
        # base cases
        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False

        d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True

        for p_idx in range(1, p_len + 1):
            # current character in pattern is '*'
            if p[p_idx - 1] == '*':
                s_idx = 1
                # d[p_idx - 1][s_idx - 1] is a string-pattern match
                # on the previous step, (one character before)
                # find the first index in string with previous match
                while not d[p_idx-1][s_idx-1] and s_idx < s_len + 1:
                    s_idx += 1
                d[p_idx][s_idx-1] = d[p_idx - 1][s_idx - 1]
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx - 1] == '?':
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
            else:
                for s_idx in range(1, s_len + 1):
                    # match is possible if there is a previous match and current characters are the same
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]
        return d[p_len][s_len]