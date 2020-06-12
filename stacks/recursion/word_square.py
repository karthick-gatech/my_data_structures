class Solution(object):
    def __init__(self, grid):
        self.grid = grid

    def word_square(self, row_num, col_num):
        if row_num == len(self.grid) - 1 and col_num == len(self.grid) - 1:
            return True
        i = col_num
        while i < len(self.grid):
            if self.grid[row_num][i] != self.grid[i][row_num]:
                return False
            i = i + 1
        return self.word_square(row_num+1, col_num+1)

# Backtracking.
# we construct the word square row by row from top to down.
# At each row, we simply do trial and error, i.e. we try with one word,
# if it does not meet the constraint then we try another one.


class Solution2:

    def wordSquares(self, words):

        self.words = words
        self.N = len(words[0])

        results = []
        word_squares = []
        for word in words:
            # try with every word as the starting word
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self, step, word_squares, results):

        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        # find out all words that start with the given prefix
        for candidate in self.getWordsWithPrefix(prefix):
            # iterate row by row
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        for word in self.words:
            if word.startswith(prefix):
                yield word

# Backtracking with hash table
# We could simply build a hashtable with all possible prefixes as keys and
# words that are associated with the prefix as the values in the table.
# we should be able to list all the words with the given prefix in constant time \mathcal{O}(1)O(1).


def buildPrefixHashTable(self, words):
    self.prefixHashTable = {}
    for word in words:
        for prefix in (word[:i] for i in range(1, len(word))):
            self.prefixHashTable.setdefault(prefix, set()).add(word)

def getWordsWithPrefix(self, prefix):
    if prefix in self.prefixHashTable:
        return self.prefixHashTable[prefix]
    else:
        return set([])

def main():
    input = ['BALL', 'AREA', 'LEAD', 'LADY']
    s = Solution(input)
    print s.word_square(0, 0)
    input_1 = ['BAB', 'AAA', 'BAB']
    s = Solution(input_1)
    print s.word_square(0, 0)
    input_1 = ['THAT', 'HASH', 'ASIA', 'THAT']
    s = Solution(input_1)
    print s.word_square(0, 0)


main()