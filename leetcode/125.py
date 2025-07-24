def isPalindrome(s: str) -> bool:   
    s = ''.join(c.lower() for c in s if c.isalnum())
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))