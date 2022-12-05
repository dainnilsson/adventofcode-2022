def solve(data, log):
    lines = data.splitlines()
    s = lines.index("")
    a = {}
    for i in range(1, len(lines[0]), 4):
        cs = []
        for j in range(s - 1):
            c = lines[j][i]
            if c != " ":
                cs.append(c)
        a[i // 4 + 1] = cs
    b = a.copy()
    for i in range(s + 1, len(lines)):
        ps = lines[i].split()
        n, f, t = (int(ps[y]) for y in (1, 3, 5))
        y, a[f] = a[f][:n], a[f][n:]
        a[t] = y[::-1] + a[t]
        y, b[f] = b[f][:n], b[f][n:]
        b[t] = y + b[t]
    yield "".join(a[k][0] for k in a)
    yield "".join(b[k][0] for k in b)
