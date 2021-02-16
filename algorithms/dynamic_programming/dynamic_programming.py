
def add_to_80():
    cache = dict()

    def calculation(n):
        if n in cache:
            return cache[n]
        else:
            print('some really expensive calculation...')
            cache[n] = 80 + n
            return cache[n]

    return calculation


memoized = add_to_80()

m = memoized(5)
print(m)
m = memoized(6)
print(m)
m = memoized(5)
print(m)