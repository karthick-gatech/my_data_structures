def count_substring(str1, str2, i):
    try:
        n2 = len(str2)
        i = str1.index(str2, i)
    except ValueError:
        return 0
    #return count_substring(str1, str2, i + n2) + 1
    return count_substring(str1, str2, i + 1) + 1


str1 = "geeksforgeeks"
str2 = "geeks"
res = count_substring(str1, str2, 0)
print res

str1 = "aaaaaaaa"
str2 = "aa"
res = count_substring(str1, str2, 0)
print res