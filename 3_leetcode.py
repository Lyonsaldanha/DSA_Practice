def lengthOfLongestSubstring(string) -> int:
    hash_set = set()
    l = 0
    res = 0

    for r in range(len(string)):
        while string[r] in hash_set:
            hash_set.remove(string[l])
            l += 1

        hash_set.add(string[r])
        res = max(res, r - l + 1)

    return res


strings = ["abcabcbb","bbbbb","pwwkew",' ',"abcabcbb"]

for s in strings:
    print(lengthOfLongestSubstring(s))