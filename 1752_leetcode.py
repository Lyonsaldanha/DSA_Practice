from collections import  deque
'''
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
'''

def check(nums):
    smallest = nums[0]
    smallest_index = 0

    for i,n in enumerate(nums):
        print(i,n,'checking',smallest >= n)
        if smallest >= n:
            smallest = n
            smallest_index =i
    if i > 0:
        before_smallest = nums[smallest_index:]
        after_smallest = nums[:smallest_index ]
        result = before_smallest + after_smallest
    return result == sorted(result)


def check(nums):
    sorted_array = sorted(nums)
    n = len(nums)
    result = []
    indices = []
    print(sorted_array)
    for x in range(1,n):
        for i in range(n):
            index = (i+x) % n
            result.append(sorted_array[index])
            print(result)
            indices.append(index)
        print(list(zip(result,indices)))
        if nums == result:
            return True
        print(result)
        del result
        result = []
    return False








print(check([3,4,5,1,2]))
print(check( nums = [2,1,3,4]))