from collections import defaultdict
def topKFrequent(nums,k):
        res = defaultdict(int)
        sorted_res = defaultdict(int)
        l = []
        for i in nums:
            res[i] += 1
        print(res)
        values = sorted(res.values())
        print(values)
        for i in values:
            for key in res.keys():
                if res[key] == i:
                    sorted_res[key] = i
                  
        return sorted_res
print(topKFrequent([1,1,1,2,2,3,4],2))