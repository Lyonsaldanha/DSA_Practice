
def isArraySpecial(nums) -> bool:
    def is_even(nums):
        return nums % 2 == 0

    if len(nums) == 1:
        return True
    l, r = 0, 1
    while r < len(nums):
        if is_even(nums[l]):
            if not is_even(nums[r]):
                l += 1
                r += 1
                print(1)
            else:
                print(2)
                return False

        else:
            if is_even(nums[r]):
                print(3)
                l += 1
                r += 1
            else:
                print(4)
                return False

    return True
