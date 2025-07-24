# First Soltuion
def strStr(haystack: str, needle: str) -> int:
    len1 = len(haystack)
    len2 = len(needle)

    if haystack == needle:
        return 0

    for i in range(1 + len1 - len2):
        if needle == haystack[i:i+len2]:
            return i
    return -1

print(strStr("abc", "c"))

# best solution
def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1