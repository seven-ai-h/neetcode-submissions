class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        store = {}
        for i in s:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1
        
        for i in t:
            if i in store:
                store[i] -= 1
            
        
        return (all(v == 0 for v in store.values()))