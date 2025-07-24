def lengthOfLastWord(s: str) -> int:
    wordFound = False
    k = 0
    for i in range(len(s)):
        if s[len(s)-i-1] != ' ' and not wordFound:
            wordFound = True
        if wordFound and s[len(s)-i-1] != ' ':
            k += 1
        if wordFound and s[len(s)-i-1] == ' ':
            return k
    return k


print(lengthOfLastWord("Hello World"))


#another solution
def lengthOfLastWord(self, s: str) -> int:                
    end = len(s) - 1

    while s[end] == " ":
        end -= 1
    
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
    
    return end - start