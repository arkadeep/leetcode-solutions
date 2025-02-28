class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        output = []
        q = collections.deque()     # we will be storing the index in this 
        r = l = 0
        
        # iterate while we are within bounds
        while r < len(nums):

            # We will pop smaller values from the queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)


            # remove left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output





