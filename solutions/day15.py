def solve(data, log):
    bs = {}
    for line in data.splitlines():
        s = line.split()
        bs[(int(s[2][2:-1]), int(s[3][2:-1]))] = int(s[8][2:-1]), int(s[9][2:])

    def scan(sy):
        rs = []
        for (x, y), (bx, by) in bs.items():
            d = abs(x - bx) + abs(y - by)
            dy = abs(y - sy)
            if dy <= d:
                dx = d - dy
                rs.append(range(x - dx, x + dx + 1))
        rs.sort(key=lambda r: (r.start, r.stop))
        while 1:
            for i in range(len(rs) - 1):
                a, b = rs[i : i + 2]
                if b.start <= a.stop:
                    rs[i] = range(a.start, max(a.stop, b.stop))
                    rs.pop(i + 1)
                    break
            else:
                return rs

    k = 2000000
    rs = scan(k)
    yield sum(len(r) for r in rs) - len(set(x for x, y in bs.values() if y == k))

    for j in range(2 * k):
        rs = scan(j)
        if len(rs) > 1:
            yield 4000000 * rs[0].stop + j
            break
