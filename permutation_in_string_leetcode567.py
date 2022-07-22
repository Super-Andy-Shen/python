#my original solution
from collections import defaultdict
class Solution:
    def match(self,dict1,dict2):
        for k,v in dict1.items():
            if dict2[k] != v:
                return False
        return True
            
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mydict1 = defaultdict(int)
        mydict2 = defaultdict(int)
        for c in s1:
            mydict1[c] += 1
        i = 0
        j = len(s1) - 1
        if len(s1) > len(s2):
            return False
        for w in range(len(s1)):
            mydict2[s2[w]] += 1
        while j < len(s2):
            if self.match(mydict1,mydict2):
                return True
            else:
                j += 1
                if j >=len(s2):
                    break
                mydict2[s2[j]] += 1
                mydict2[s2[i]] -= 1
                i += 1
        return False
            
            