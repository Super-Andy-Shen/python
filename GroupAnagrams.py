from collections import defaultdict
# brutal force method
def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for i in range(len(t)):
                s = s.replace(t[i],'',1)
            if len(s) > 0:
                return False
            else:
                return True
def groupAnagrams(strs):
        res = []
        while(len(strs) > 0):
            lista = []
            first_str = strs.pop(0)
            lista.append(first_str)
        
            for i in range(len(strs)):
                 if isAnagram(first_str,strs[i]):
                    lista.append(strs[i]) 
            for j in range(1,len(lista)):
                    strs.remove(lista[j])
            res.append(lista)
        return res
# Hashmap Method
def groupAnagrams(strs):
        res = defaultdict(list)
        
        for s in strs:
            key_tuple = [0]*26
            for c in s:
                key_tuple[ord(c) - ord('a')] += 1
            res[tuple(key_tuple)].append(s)
        
        return res.values()
            
