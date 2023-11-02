def gcd(*args):
    def _gcd(n, m):
        if m == 0:
            return n
        else:
            return _gcd(m, n % m)

    if len(args) < 2:
        return args[0]
    else:
        n = args[0]
        for m in args[1:]:
            n = _gcd(n, m)
        return n


def lcm(*args):
    def _lcm(n, m):
        return n * m // gcd(n, m)

    if len(args) < 2:
        return args[0]
    else:
        n = args[0]
        for m in args[1:]:
            n = _lcm(n, m)
        return n


n, m = map(int, input().split())

print(gcd(n, m))
print(lcm(n, m))