def solve(data, log):
    m, v = {}, {}
    for ln in data.splitlines():
        k, n = ln.split(": ")
        try:
            v[k] = int(n)
        except Exception:
            m[k] = n.split()
    os = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    r = lambda k: v[k] if k in v else os[m[k][1]](r(m[k][0]), r(m[k][2]))

    yield int(r("root"))

    def c(i):
        v["humn"] = i
        a, _, b = m["root"]
        a, b = r(a), r(b)
        return 1 if a > b else -1 if a < b else 0

    b, n, s = 0, 0, c(0)
    while s == c(1 << n):
        n += 1

    for i in range(n, 0, -1):
        a = 1 << (i - 1)
        if c(b + a) != -s:
            b += a
    yield b
