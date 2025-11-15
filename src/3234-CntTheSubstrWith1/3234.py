# Solution
def dominantSubstring(s: str) -> int:
    n = len(s)
    a = [1 if c == '1' else 0 for c in s]

    prefix = [0]
    for x in a:
        prefix.append(prefix[-1] + x)

    ans = 0
    # 枚举 zeros 的数量 z
    # zeros^2 <= n → z <= sqrt(n)
    import math
    max_z = int(math.sqrt(n)) + 2

    for z in range(max_z + 1):
        # ones >= z^2
        need = z * z

        # two pointers: count substrings with exactly z zeros,
        # and ones >= need
        cnt_zero = 0
        l = 0
        zero_pos = []

        for r in range(n):
            if s[r] == '0':
                cnt_zero += 1
                zero_pos.append(r)

            # 若 zeros > z，移动左指针
            while cnt_zero > z:
                if s[l] == '0':
                    cnt_zero -= 1
                    zero_pos.pop(0)
                l += 1

            # 现在区间 [l..r] 中 zeros ≤ z
            # 若 zeros == z，则检查 ones
            if cnt_zero == z:
                ones = prefix[r+1] - prefix[l]
                if ones >= need:
                    ans += 1

    return ans