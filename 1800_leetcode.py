def maxAscendingSum(nums) -> int:
    if len(nums) <= 1:
        return nums[0]
    res = []
    max_total = 0
    total = nums[0]
    for i in range(1,len(nums)):
        if nums[i] <= nums[i - 1]:
            max_total = max(total, max_total)
            total = 0
        total += nums[i]

    return max(max_total,total)


test_cases = [[10,20,30,5,10,50],[10,20,30,40,50],[12,17,15,13,10,11,12],[1,2,3,4,5,6,7,8,9,10]]

for t in test_cases:
    print(maxAscendingSum(t),'answer')


