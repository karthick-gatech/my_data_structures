class Solution(object):
    def __init__(self, input, dictionary):
        self.input = input
        self.dictionary = dictionary

    def find_word_break(self):
        word_break = [False] * (len(self.input) + 1)
        word_break[0] = True
        i, j = 0, 0
        while i < len(self.input) + 1:
            j = 0
            while j < i:
                if not word_break[j]:
                    j = j + 1
                    continue
                if self.input[j:i] in self.dictionary:
                    word_break[i] = True
                    break
                j = j + 1
            i = i + 1
        return word_break[len(self.input)]

def main():
    s = Solution("wordA", ['A', 'word', 'search'])
    if s.find_word_break():
        print "Words were split"
    else:
        print "Not split"


main()