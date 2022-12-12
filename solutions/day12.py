def solve(data, log):
    m, b = {}, []
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "a":
                b.append((x, y))
            elif c == "S":
                a = x, y
                c = "a"
            elif c == "E":
                e = x, y
                c = "z"
            m[(x, y)] = ord(c) - 97

    def f(s):
        v, tv = set(), [(s, 0, 1)]
        while tv:
            (x, y), l, t = tv.pop(0)
            for nx, ny in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                n = nx, ny
                nl = m.get((nx, ny), 26)
                if nl < l + 2 and n not in v:
                    if n == e:
                        return t
                    v.add(n)
                    tv.append((n, nl, t + 1))

    yield f(a)
    yield min(filter(bool, (f(s) for s in b)))
