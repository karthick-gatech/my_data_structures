# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# brute force
# generate all 2^(2*n) sequences of ( and ). Check if each one is valid
# To check whether a sequence is valid, we keep track of balance,
# the net number of opening brackets minus closing brackets.
# If it falls below zero at any time, or doesn't end in zero, the sequence is invalid


class Solution(object):
    def generateParenthesis(self, n):
        def generate(A=[]):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

# backtracking
# instead of adding ( and ) everytime, only add them when it will remain a valid
# sequence. We can do this by keeping track of number of opening and closing
# brackets. We can start an opening bracket if we still have one (of n) left to place.
# And we can start a closing bracket if it would not exceed the number of opening brackets.


class Solution2(object):
    def generateParenthesis(self, N):
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
