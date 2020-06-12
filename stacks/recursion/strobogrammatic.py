# A strobogrammatic number is a number that looks the same
# when rotated 180 degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
#
# Input:  n = 2
# Output: ["11","69","88","96"]


def findStrobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    evenMidCandidate = ["11", "69", "88", "96", "00"]
    oddMidCandidate = ["0", "1", "8"]
    if n == 1:
        return oddMidCandidate
    if n == 2:
        return evenMidCandidate[:-1]
    if n % 2:
        pre, midCandidate = findStrobogrammatic(n - 1), oddMidCandidate
    else:
        pre, midCandidate = findStrobogrammatic(n - 2), evenMidCandidate
    premid = (n - 1) / 2
    return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]


print findStrobogrammatic(3)
print findStrobogrammatic(5)