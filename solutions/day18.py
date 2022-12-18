def solve(data, log):
    def ns(p):
        for i in range(3):
            for j in -1, 1:
                yield p[:i] + (p[i] + j,) + p[i + 1 :]

    m = {tuple(int(c) for c in ln.split(",")) for ln in data.splitlines()}
    yield sum(sum(1 for n in ns(p) if n not in m) for p in m)
    rs = [range(min(p[i] for p in m) - 1, max(p[i] for p in m) + 2) for i in range(3)]
    q = [tuple(r.start for r in rs)]
    v, b = set(q), 0
    while q:
        for n in ns(q.pop(0)):
            if all(n[i] in rs[i] for i in range(3)):
                if n in m:
                    b += 1
                elif n not in v:
                    v.add(n)
                    q.append(n)
    yield b
