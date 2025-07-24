from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = {}

    for word in strs:
        key = tuple(sorted(word))
        if key not in res:
            res[key] = []
        res[key].append(word) 
        print(res)

    return list(res.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())