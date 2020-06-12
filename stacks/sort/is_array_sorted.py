class Solution(object):
    def __init__(self, input):
        self.input = input

    def is_sorted(self, start=0):
        if start == len(self.input) - 1:
            return True
        if self.input[start] <= self.input[start+1]:
            return self.is_sorted(start+1)
        else:
            return False

def main():
    input = [0,0]
    s = Solution(input)
    if s.is_sorted():
        print "Array is sorted"
main()
