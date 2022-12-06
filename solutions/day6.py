def solve(data, log):
    r = range(len(data))
    s = lambda x: next(i for i in r if len(set(data[i : i + x])) == x) + x
    yield s(4)
    yield s(14)
