class Solution(object):
    def __init__(self, input):
        self.input_array = input
        self.output_array = []

    def remove_duplicates(self):
        i = 0
        while i < len(self.input_array):
            j = i + 1
            self.output_array.append(self.input_array[i])
            while j < len(self.input_array) and self.output_array[-1] == self.input_array[j]:
                j = j + 1
            if j != i + 1:
                self.output_array.append(self.input_array[i])
            i = j

    def remove_duplicates_in_place(self):
        if len(self.input_array) <= 2:
            return None
        i = 1
        while i + 1 < len(self.input_array):
            print self.input_array[i]
            print self.input_array[i+1]
            if self.input_array[i] == self.input_array[i+1]:
                del self.input_array[i+1]
            i = i + 1


def main():
    s = Solution([1,1,1,2,2,3])
    s.remove_duplicates()
    print s.output_array
    print s.input_array
    s.remove_duplicates_in_place()
    print s.input_array


main()
