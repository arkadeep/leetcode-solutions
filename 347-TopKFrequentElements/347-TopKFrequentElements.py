class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        val_based_rev = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}

        return (list(val_based_rev.keys()))[0:k]