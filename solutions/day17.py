def solve(data, log):
    data = data.strip()
    wn, v = len(data), [0, 0, 0, 0, {(x, 0) for x in range(7)}]
    rs = (
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
        ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
    )

    def d(dx=2, dy=4, my=0):
        r = rs[v[2]]

        def t(dx, dy):
            t = tuple((x + dx, y + dy) for (x, y) in r)
            return all(0 <= x < 7 for (x, _) in t) and not any(p in v[4] for p in t)

        v[2] = (v[2] + 1) % 5
        while 1:
            w = -1 if data[v[3]] == "<" else 1
            v[3] = (v[3] + 1) % wn
            if t(dx + w, dy):
                dx += w
            if t(dx, dy - 1):
                dy -= 1
            else:
                my = max(max(y + dy for _, y in r), my)
                v[4] |= {(x + dx, y + dy) for x, y in r}
                break
        v[0] += 1
        v[1] += my
        v[4] = {(x, y - my) for (x, y) in v[4] if y > my - 40}

    for _ in range(2022):
        d()
    yield v[1]

    si, so = v[:2]
    s = lambda: (*v[2:4], frozenset(x for (x, y) in v[4] if not y))
    m, _ = s(), d()
    while s() != m:
        d()
    di, b = v[0] - si, v[1] - so
    k, r = divmod(1000000000000 - v[0], di)
    for _ in range(r):
        d()
    yield k * b + v[1]
