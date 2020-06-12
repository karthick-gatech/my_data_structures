import sys


class Solution(object):
    def __init__(self, input):
        self.input = input
        self.length_of_rod = len(input)

    def cutRod(self, index):
        if index <= 0:
            return 0
        max_val = -sys.maxsize-1
        # recursively cut the rod in different pieces
        # and compare different configurations.
        for i in range(0, index):
            #print "Before recursing for {}".format(index-i-1)
            max_val = max(max_val, self.input[i] + self.cutRod(index-i-1))
            #print "After recursion for {}".format(index-i-1)
        return max_val

    def dynamic_programming(self):
        val = [0 for x in range(len(self.input)+1)]
        val[0] = 0
        max_val = -sys.maxsize-1
        for i in range(1, len(self.input)+1):
            curr_max_val = max_val
            for j in range(i):
                curr_max_val = max(curr_max_val, self.input[j] + val[i-j-1])
            val[i] = curr_max_val
        return val[len(self.input)]

def main():
    s = Solution([10,2,6,4])
    print s.cutRod(s.length_of_rod)
    print s.dynamic_programming()


main()