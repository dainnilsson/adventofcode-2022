def solve(data, log):
    cm = lambda xs: set(xs[0]) & cm(xs[1:]) if len(xs) > 1 else set(xs[0])
    ps = lambda x: 1 + ord(x) - (ord("a") if x.islower() else (ord("A") - 26))
    ls = data.splitlines()
    yield sum(ps(cm([ln[: len(ln) // 2], ln[len(ln) // 2 :]]).pop()) for ln in ls)
    yield sum(ps(cm([ls[i + j] for j in range(3)]).pop()) for i in range(0, len(ls), 3))
