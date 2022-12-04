def solve(data, log):
    a, b = 0, 0
    for line in data.splitlines():
        (s1, e1), (s2, e2) = ((int(y) for y in x.split("-")) for x in line.split(","))
        if s1 <= s2 and e1 >= e2 or s2 <= s1 and e2 >= e1:
            a += 1
        if s1 <= s2 and e1 >= s2 or s2 <= s1 and e2 >= s1:
            b += 1
    yield a
    yield b
