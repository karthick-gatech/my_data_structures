import copy


class Solution(object):
    def __init__(self, input):
        self.input_array = copy.deepcopy(input)

    def find_word_exists(self, word):
        for row in range(len(self.input_array)):
            for col in range(len(self.input_array[0])):
                if self.dfs(word, row, col, 0):
                    return True
        return False

    def dfs(self, word, row, col, curr_len):
        if row < 0 or col < 0 or row >= len(self.input_array) or col >= len(self.input_array[0]):
            return False
        if self.input_array[row][col] == word[curr_len]:
            c = self.input_array[row][col]
            self.input_array[row][col] = '#'

            if curr_len == len(word) - 1:
                return True
            elif self.dfs(word, row - 1, col, curr_len + 1) or self.dfs(word, row + 1, col, curr_len + 1) or \
                    self.dfs(word, row, col - 1, curr_len + 1) or self.dfs(word, row, col + 1, curr_len + 1):
                return True
            self.input_array[row][col] = c
        return False


def main():
    input = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
    for word in ['ABCCED','ABCES', 'SFCSE']:
        s = Solution(input)
        if s.find_word_exists(word):
            print "Word {} exists".format(word)
        else:
            print "Word {} doesnt exist".format(word)


main()