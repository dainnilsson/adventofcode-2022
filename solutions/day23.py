def solve(data, log):
    ln = data.splitlines()
    h, w = len(ln), len(ln[0])
    e = {(x, y) for y in range(h) for x in range(w) if ln[y][x] == "#"}
    ds, a = [(0, -1), (0, 1), (-1, 0), (1, 0)], (-1, 0, 1)

    def s():
        m = {}
        for x, y in e:
            if all(((x + dx, y + dy) not in e for dx in a for dy in a if dx or dy)):
                continue
            for dx, dy in ds:
                if all((x + (dx or i), y + (dy or i)) not in e for i in a):
                    d = x + dx, y + dy
                    m[d] = (x, y) if d not in m else None
                    break
        m = {d: o for d, o in m.items() if o}
        for d, o in m.items():
            e.remove(o)
            e.add(d)
        ds.append(ds.pop(0))
        return m

    b, x1, x2, y1, y2 = 10, w, 0, h, 0
    for _ in range(b):
        s()
    for x, y in e:
        x1, x2, y1, y2 = min(x, x1), max(x, x2), min(y, y1), max(y, y2)
    yield (x2 - x1 + 1) * (y2 - y1 + 1) - len(e)
    while s():
        b += 1
    yield b + 1
