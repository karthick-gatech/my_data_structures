class Solution(object):
    def __init__(self, input):
        self.input = input

    def string_reverse(self, index=0):
        if index >= len(self.input):
            return ""
        return self.string_reverse(index + 1) + self.input[index]


def main():
    s = Solution("abcdefgh")
    print s.string_reverse()

    s = Solution("a")
    print s.string_reverse()

    s = Solution("")
    print s.string_reverse()

    s = Solution("abc")
    print s.string_reverse()

    s = Solution("     ")
    print s.string_reverse()

main()