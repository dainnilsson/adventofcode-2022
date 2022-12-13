def solve(data, log):
    def c(a, b):
        if type(a) == int:
            return a - b if type(b) == int else c([a], b)
        else:
            if type(b) == int:
                return c(a, [b])
            if a and b:
                return c(a[0], b[0]) or c(a[1:], b[1:])
            return 1 if a else -1 if b else 0

    ps = [eval(p) for p in data.splitlines() if p]
    yield sum(i // 2 + 1 for i in range(0, len(ps), 2) if c(*ps[i : i + 2]) < 0)
    a = sum(1 for p in ps if c(p, [[2]]) < 0) + 1
    b = sum(1 for p in ps if c(p, [[6]]) < 0) + 2
    yield a * b
