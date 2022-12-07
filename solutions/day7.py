def solve(data, log):
    p, ds, fs = (), {}, {}
    for line in data.splitlines():
        ps = line.split()
        if ps[0] == "$":
            if ps[1] == "cd":
                d = ps[2]
                p = () if d == "/" else p[:-1] if d == ".." else p + (d,)
        else:
            d = p + (ps[1],)
            ds.setdefault(p, []).append(d)
            if ps[0] != "dir":
                fs[d] = int(ps[0])
    w = lambda k: fs[k] if k in fs else sum(w(v) for v in ds[k])
    ws = [w(k) for k in ds]
    yield sum(v for v in ws if v <= 100000)
    r = max(ws) - 40000000
    yield min(v for v in ws if v >= r)
