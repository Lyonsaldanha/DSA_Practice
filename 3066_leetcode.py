import heapq
def minOperations(nums,k):

    heapq.heapify([nums])
    print(nums)
    while nums[0] <= k:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        print(x,y)
        new_value = 2*min(x,y) + max(x,y)
        heapq.heappush(nums,new_value)
        print(nums)
    return nums
nums = [2,11,10,1,3]
nums.sort()
print(minOperations(nums,k=10))