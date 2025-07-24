def isPalindrome(s: str) -> bool:
    word = ""
    for i in s:
        if i.isalnum():
            word += i.lower()
    
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

print(isPalindrome("tab a cat"))