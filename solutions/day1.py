def solve(data, log):
    c = 0
    cs = []

    for line in data.splitlines():
        if line:
            c += int(line)
        else:
            cs.append(c)
            c = 0

    cs.sort()
    yield cs[-1]
    yield sum(cs[-3:])
