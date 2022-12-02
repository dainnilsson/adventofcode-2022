def solve(data, log):
    ps = lambda a, b: 1 + b + ((b - a + 1) % 3) * 3
    sa, sb = 0, 0
    for line in data.splitlines():
        x, y = line.split()
        xv = ord(x) - ord("A")
        yv = ord(y) - ord("X")
        sa += ps(xv, yv)
        sb += ps(xv, (xv + yv - 1) % 3)
    yield sa
    yield sb
