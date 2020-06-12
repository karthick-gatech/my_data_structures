class Solution(object):
    def __init__(self, input, sum):
        self.input_list = input
        self.sum = sum

    def subset_sum(self, input, n, sum):
        if sum == 0:
            return True
        if n == 0 and sum != 0:
            return False
        # either include the last element or
        # dont include the element.
        return self.subset_sum(input, n-1, sum) or self.subset_sum(input, n-1, sum-input[n-1])

    def dynamic_program(self):
        subset = [[False for i in range(sum+1)] for i in range(n+1)]
        for i in range(n+1):
            subset[i][0] = True
        for i in range(1, sum+1):
            subset[0][i] = False
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if j < self.input_list[i-1]:
                    subset[i][j] = subset[i-1][j]
                if j >= self.input_list[i-1]:
                    subset[i][j] = subset[i-1][j] or subset[i-1][j-self.input_list[i-1]]
        return subset[n][sum]

def main():
    input = [3, 34, 4, 12]
    sum = 12
    s = Solution(input, sum)
    print s.subset_sum(input, len(input), sum)
    s.dynamic_program()


main()