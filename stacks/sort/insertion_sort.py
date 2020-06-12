import copy
from heapq import heappop, heappush, heapify

class Solution(object):
    def __init__(self, input):
        self.input = input

    def insertion_sort(self):
        print "Unsorted array: {}".format(self.input)
        sorted_array = copy.copy(self.input)
        i, j = 0, 0
        while i < len(sorted_array):
            j = i
            while j > 0:
                if sorted_array[j] < sorted_array[j-1]:
                    print 'Going into swap routine'
                    temp = sorted_array[j]
                    sorted_array[j] = sorted_array[j-1]
                    sorted_array[j-1] = temp
                j = j - 1
            i = i + 1
        print "Sorted array: {}".format(sorted_array)

    def heap_sort(self, k):
        sorted_array = [0] * len(self.input)
        heap = self.input[:k+1]
        heapify(heap)
        target_index = 0
        for rem_elements_index in range(k+1, len(self.input)):
            popped_element = heappop(heap)
            sorted_array[target_index] = popped_element
            heappush(heap, self.input[rem_elements_index])
            target_index += 1

        while heap:
            popped_element = heappop(heap)
            sorted_array[target_index] = popped_element
            target_index += 1

        print "Sorted array: {}".format(sorted_array)


def main():
    s = Solution([3,4,2,1])
    s.insertion_sort()

    s = Solution([1, 2, 3, 4])
    s.insertion_sort()

    s = Solution([2, 6, 3, 12, 56, 8])
    s.heap_sort(3)

    s = Solution([3, 5, 2, 1])
    s.heap_sort(2)

main()