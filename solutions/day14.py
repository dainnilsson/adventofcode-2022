def solve(data, log):
    m = set()
    for line in data.splitlines():
        ps = [[int(v) for v in p.split(",")] for p in line.split(" -> ")]
        x, y = ps.pop(0)
        for nx, ny in ps:
            while 1:
                m.add((x, y))
                dx, dy = nx - x, ny - y
                x += dx // abs(dx) if dx else 0
                y += dy // abs(dy) if dy else 0
                if dx == dy == 0:
                    break

    def f():
        x, y = 500, 0
        while y < h:
            for dx in 0, -1, 1:
                if (x + dx, y + 1) not in m:
                    x += dx
                    y += 1
                    break
            else:
                break
        m.add((x, y))
        return y

    c, h = 0, max(p[1] for p in m) + 1
    while f() < h:
        c += 1
    yield c

    while f():
        c += 1
    yield c + 2
