
def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    else:
        count_1 = {}
        count_2 = {}
        num_diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                num_diff += 1
                if num_diff > 2:
                    return False

            count_1[s1[i]] = count_1.get(s1[i], 0) + 1
            count_2[s2[i]] = count_2.get(s2[i], 0) + 1

        return count_1 == count_2




