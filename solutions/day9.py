def solve(data, log):
    def m(d, s={"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}):
        hx, hy = n[0]
        dx, dy = s[d]
        n[0] = hx + dx, hy + dy

    def f(i):
        (hx, hy), (tx, ty) = n[i - 1], n[i]
        dx, dy = hx - tx, hy - ty
        if max(abs(dx), abs(dy)) > 1:
            if dx != 0:
                tx += dx // abs(dx)
            if dy != 0:
                ty += dy // abs(dy)
        n[i] = tx, ty

    p = [ln.split() for ln in data.splitlines()]
    for k in (2, 10):
        n = [(0, 0)] * k
        v = set()
        for d, i in p:
            for _ in range(int(i)):
                m(d)
                for j in range(1, k):
                    f(j)
                v.add(n[-1])
        yield len(v)
