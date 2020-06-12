# Given a file and assume that you can only read the file using a given method read4,
# implement a method read to read n characters. Your method read may be called multiple times.
#
#
#
# Method read4:
#
# The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
#
# The return value is the number of actual characters read.
#
# Note that read4() has its own file pointer, much like FILE *fp in C.
# Parameter:  char[] buf
#     Returns:    int
#
# Note: buf[] is destination not source, the results from read4 will be copied to buf[]

# File file("abc");
# Solution sol;
# // Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.

# Input: file = "leetcode", n = 5
# Output: 5
# Explanation: After calling your read method, buf should contain "leetc".
# We read a total of 5 characters from the file, so return 5.


# Input: file = "abcde", n = 5
# Output: 5
# Explanation: After calling your read method, buf should contain "abcde".
# We read a total of 5 characters from the file, so return 5.

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        idx = 0
        while n > 0:
            # read file to buf4
            buf4 = [""]*4
            l = read4(buf4)
            # if no more char in file, return
            if not l:
                return idx
            # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[idx] = buf4[i]
                idx += 1
                n -= 1
        return idx