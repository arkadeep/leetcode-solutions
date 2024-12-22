class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # A linear time solution is possible using bucket sorting
        # Indices are going to be the count
        # The values associated with each index are going to be the numbers
        # For example if a number appears once - the 1th index will contain the number which
        # occurred once

        count = {}

        # This contains the buckets which will hold the numbers according to their frequency
        freq = [[] for i in range(len(nums) + 1)]
        
        # Populating the hash map, which stores the frequency of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Populating the array
        for n, c in count.items():
            
            # Each index of the array is the frequency count - 
            # And associated with each frequency count, we have the numbers, stored in a list,
            # that appear that many times
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            # Note that each index is associated with a list
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        # This is a O(n log n) solution since it relies on sorting
        # d = {}
        
        # for i in nums:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1

        # val_based_rev = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse = True)}

        # return (list(val_based_rev.keys()))[0:k]