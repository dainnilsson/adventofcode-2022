def solve(data, log):
    s, ms = [], []
    ln = [""] + data.splitlines()
    while ln:
        ln = ln[2:]
        s += [([int(x) for x in ln.pop(0)[17:].split(",")], 0)]
        o, a = ln.pop(0).split()[-2:]
        a = 0 if a == "old" else int(a)
        ms += [[o, a, *[int(ln.pop(0).split()[-1]) for _ in range(3)]]]

    def r(s, n, t):
        for _ in range(n):
            for i, (o, a, b, c, d) in enumerate(ms):
                for y in s[i][0]:
                    y = t(y + (a or y) if o == "+" else y * (a or y))
                    j = c if y % b == 0 else d
                    s[j] = s[j][0] + [y], s[j][1]
                s[i] = [], s[i][1] + len(s[i][0])
        a = [x[1] for x in s]
        a.sort()
        return a[-1] * a[-2]

    yield r(s[:], 20, lambda x: x // 3)
    d = 1
    for m in ms:
        d *= m[2]
    yield r(s, 10000, lambda x: x % d)
