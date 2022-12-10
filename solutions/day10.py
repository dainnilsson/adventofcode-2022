def solve(data, log):
    def t():
        d[a[0] // 40] += "#" if abs((a[0] % 40) - a[1]) < 2 else "."
        a[0] += 1
        if a[0] % 40 == 20:
            a[2] += a[0] * a[1]

    a = [0, 1, 0]
    d = [""] * 6
    for line in data.splitlines():
        t()
        if line[0] == "a":
            t()
            a[1] += int(line.split()[1])
    yield a[2]
    yield "\n".join(d)
