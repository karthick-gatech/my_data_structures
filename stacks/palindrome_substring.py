class Solution(object):
    def __init__(self, s):
        self.input = s

    def find_longest_palindrome(self):
        if not self.input or len(self.input) < 2:
            return self.input

        length = len(self.input)
        is_palindrome = [[False] * length for i in range(length)]
        left, right = 0, 0
        i, j = 0, 1
        while j < length:
            i = 0
            while i < j:
                #print i + 1, j - 1
                is_inner_palindrome = is_palindrome[i+1][j-1] or (j - i) <= 2
                if self.input[i] == self.input[j] and is_inner_palindrome:
                    is_palindrome[i][j] = True
                    if j - i > right - left:
                        left = i
                        right = j
                i = i + 1
            j = j + 1

        print is_palindrome
        print self.input[left:right+1]


def main():
    s = Solution('bacddcab')
    s.find_longest_palindrome()

main()