#my original solution
# from collections import defaultdict
# class Solution:
#     def checking(self,dict_s,dict_t):
#         for k , v in dict_t.items():
#             if dict_s[k] < v:
#                 return False
#         return True
#     def minWindow(self, s: str, t: str) -> str:
#         mydict_s = defaultdict(int)
#         mydict_t = defaultdict(int)
#         for c in t:
#             mydict_t[c] += 1
        
#         i = 0
#         j = len(t) - 1
#         mini = len(s)
#         minis =""
#         if len(s) < len(t):
#             return minis
#         for w in range(len(t)):
#             mydict_s[s[w]] += 1
        
#         while j < len(s):
#             if self.checking(mydict_s,mydict_t):
#                 if j - i + 1 <= mini:
#                     minis = s[i:j + 1]
#                     mini = j - i + 1
#                 mydict_s[s[i]] -= 1
#                 for n in range(i+len(t)+1,j+1):
#                     mydict_s[s[n]] -= 1
#                 j = i + len(t) 
#                 i += 1
#             else:
#                 j += 1
#                 if j >= len(s):
#                     break
#                 mydict_s[s[j]] += 1
                
#         return minis
          