def longestMonotonicSubarray(nums) -> int:

    if len(nums) <= 1:
        return len(nums)
    max_length = 1
    for i in range(len(nums) - 1):
        inc_count = 0
        if nums[i] < nums[i + 1]:
            inc_count += 1
            j = i
            while j < len(nums) - 1 and nums[j] < nums[j + 1]:  # Check bounds
                inc_count += 1
                j += 1

        dnc_count = 0
        if nums[i] > nums[i + 1]:  # Decreasing sequence
            dnc_count +=1
            j = i
            while j < len(nums) - 1 and nums[j] > nums[j + 1]:  # Check bounds
                dnc_count += 1
                j += 1
        max_length  = max(max_length, inc_count, dnc_count)

    return max_length


# Test cases
test_cases = [[1, 4, 3, 3, 2], [3, 3, 3, 3], [3, 2, 1],[],[1]]

for t in test_cases:
    print(longestMonotonicSubarray(t), 'ANSWER')
