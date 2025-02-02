from collections import  deque

def check(nums) -> bool:
    sorted_array = sorted(nums)
    q = deque(sorted_array)
    q2 = deque(nums)
    i = 0
    while i < len(nums):
        if q == q2:
            return True
        if q:
            temp = q.popleft()
            q.append(temp)

        i += 1
    return False



print(check([3,4,5,1,2]))
print(check( nums = [2,1,3,4]))