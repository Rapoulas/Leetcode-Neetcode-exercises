def isAnagram(s: str, t: str) -> bool:
    arr = []
    if len(s) != len(t):
        return False
    
    for i in s:
        arr.append(i)
    
    for i in t:
        print(i)
        if i in arr:
            arr.remove(i)
        else:
            return False
    return True
            

print(isAnagram("xx", "x"))


# Best solution
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    return sorted(s) == sorted(t)

print(isAnagram("act", "cat"))