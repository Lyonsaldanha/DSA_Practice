
def myAtoi(s) -> int:
    maxR = (2 ** 31) - 1
    minR = -1 * (2 ** 31)
    res = 0
    sign = 1
    sign_set = False

    digit_not_found = True
    for r in range(len(s)):
        if s[r] == " " and digit_not_found:
            continue
        elif s[r].isalpha():
            return res
        if s[r] in ("+", "-") and digit_not_found and not sign_set:
            if s[r] == "+":
                sign_set = True
                sign = 1
            else:
                sign_set = True
                sign = -1
            continue
        if sign_set:
            break
    for r in range(r,len(s)):

        if s[r].isdigit():
            res = (res * 10) + int(s[r])
            print(s[r])
        else:
            break

    res *= sign
    if int(res) < minR:
        return minR
    elif int(res) > maxR:
        return maxR
    else:
        return int(res)


s = " -42"
print(myAtoi(s))