def solve(data, log):
    t = data.splitlines()
    w, h = len(t[0]), len(t)

    def a(x, y):
        h = t[y][x]
        return (
            all(v < h for v in t[y][:x])
            or all(v < h for v in t[y][x + 1 :])
            or all(r[x] < h for r in t[:y])
            or all(r[x] < h for r in t[y + 1 :])
        )

    s = 2 * w + 2 * h - 4
    yield s + sum(1 for x in range(1, w - 1) for y in range(1, h - 1) if a(x, y))

    def b(x, y, a=1):
        m = t[y][x]

        def c(x, y, dx, dy):
            if 0 <= x < w and 0 <= y < h:
                return 1 if t[y][x] >= m else 1 + c(x + dx, y + dy, dx, dy)
            return 0

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            a *= c(x + dx, y + dy, dx, dy)
        return a

    yield max(b(x, y) for x in range(1, w - 1) for y in range(1, h - 1))
