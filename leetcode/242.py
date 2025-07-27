def isAnagram(s: str, t: str) -> bool:
    hasherS = {}
    hasherT = {}

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        hasherS[s[i]] = 1 + hasherS.get(s[i], 0)
        hasherT[t[i]] = 1 + hasherT.get(t[i], 0)
    for c in hasherS:
        if hasherS[c] != hasherT.get(c, 0):
            return False
    return True