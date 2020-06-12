# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.


class Solution(object):
    def longestPalindrome(self, s):
        ans = ''
        max_len = 0
        n = len(s)
        DP = [[0] * n for _ in xrange(n)]
        for i in xrange(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]
        for i in xrange(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                ans = s[i:i+2]
                max_len = 2
        for j in xrange(n):
            for i in xrange(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j+1]
                        max_len = j - i + 1
        return ans


def longestPalSubstr(string):
    maxLength = 1
    start = 0
    length = len(string)
    low = 0
    high = 0
    # Step to generate odd length palindrome:
    # Fix a centre and expand in both directions for longer palindromes.
    # Step to generate even length palindrome
    # Fix two centre ( low and high ) and expand in both directions for longer palindromes.

    for i in xrange(1, length):
        # Find the longest even length palindrome with center
        # points as i-1 and i.
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1
            low -= 1
            high += 1

    print "Longest palindrome substring is:",
    print string[start:start + maxLength]

    return maxLength


# Driver program to test above functions
string = "forgeeksskeegfor"
print "Length is: " + str(longestPalSubstr(string))