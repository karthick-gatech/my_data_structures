class Solution(object):
    def __init__(self):
        pass

    def split_recursion(self, s):
        if s == "" or self.is_palindrome(s):
            return 0
        else:
            cuts = float("inf")
            i = 1
            while i < len(s):
                cuts = min(1 + self.split_recursion(s[0:i]) + self.split_recursion(s[i:len(s)]), cuts)
                i = i + 1
            return cuts

    def is_palindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False

def main():
    s = Solution()
    print s.split_recursion("xaab")
    print s.split_recursion("xaax")
    print s.split_recursion("abcd")

main()