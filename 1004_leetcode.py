def longestOnes(nums, k) -> int:
    res = 0
    i = 0
    l, r = 0, 0
    lives = k
    for n in range(len(nums)-1):
        while r < len(nums):
            if nums[r] == 0 and lives == 0 :
                print(1)
                res = max(res, r - l + 1)
                l += 1
                r = l
                lives = k
            elif nums[r] == 0 and lives > 0:
                print(2)
                lives -= 1
                r += 1
            else:
                print(3)
                r += 1
    return res



for i,k in [([0,1],1),([0,0,0,1],4)]:
    print(longestOnes(i,k))
    print("break")