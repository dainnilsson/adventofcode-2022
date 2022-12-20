def solve(data, log):
    class W:
        def __init__(s, i):
            s.i = i

    d = [int(ln) for ln in data.splitlines()]
    n = len(d)

    def m(ns, t=1):
        s = [W(n) for n in ns]
        b, m = s[:], n - 1
        for _ in range(t):
            for v in s:
                i = b.index(v)
                b.pop(i)
                b.insert((i + v.i) % m, v)
        return [v.i for v in b]

    a = m(d)
    i = a.index(0)
    yield sum(a[(i + j) % n] for j in (1000, 2000, 3000))

    b = m([n * 811589153 for n in d], 10)
    i = b.index(0)
    yield sum(b[(i + j) % n] for j in (1000, 2000, 3000))
