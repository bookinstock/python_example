# iterator

# an object that can iterated upon.

# an object that return data, one item at a time.

# build own iterator with iterable protocol

# by impl two special methods `__iter__` and `__next__`

# `iter()` function => call `__iter__()` method -> return iterator

# `next()` function => call `__next__()` method -> return next item

# when reach the end, it will raise `StopIteration`.


# where?

# - for loop

# - comprehension

# - generator

a = [1, 2, 3, 4, 5]

i = iter(a)

a1 = next(i)  # 1

a2 = next(i)  # 2

print(f"a1={a1},a2={a2}")

# for

a = [1, 2, 3, 4, 5]

for e in a:
    print(e)

# impl for

a = [1, 2, 3, 4, 5]

i = iter(a)

while True:
    try:
        e = next(i)
        print(e)
    except StopIteration:
        break

# 1
# 2
# 3
# 4
# 5

# own iterator


class A:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 * self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = A(5)
i = iter(a)
for e in i:
    print(e)

# 0
# 2
# 4
# 6
# 8
# 10

##

l = [1, 2, 3, 4, 5]

i = iter(l)

for e in i:
    print(e)


# for

a = [1, 2, 3, 4, 5]

for e in a:
    print(e)

for i, e in enumerate(a):
    print(i, e)

a = {"a": 1, "b": 2, "c": 3}

for k in a:
    print(k)

for k in a.keys():
    print(k)


for k in a:
    print(a[k])

for v in a.values():
    print(v)

for (k, v) in a.items():
    print(k, v)


a = [1, 2, 3]

b = ["a", "b", "c"]

for x, y in zip(a, b):
    print(x, y)


for e in reversed(range(0, 5)):
    print(e)

for e in range(5, 0, -1):
    print(e)


for e in sorted(range(5, 0, -1)):
    print(e)


# comprehension

[e for e in range(0, 5)]

[(e, e + 1) for e in range(0, 5)]

{(e, e + 1) for e in range(0, 5)}

{e: e + 1 for e in range(0, 5)}

a = [1, 2, 3]

b = ["a", "b", "c"]

[(x, y) for x, y in zip(a, b)]

{(x, y) for x, y in zip(a, b)}

{x: y for x, y in zip(a, b)}


# generator

(e for e in range(0, 5))

#

x = map(lambda e: e * 2, range(5))

x = map(lambda e1, e2: e1 + e2, range(1, 6), range(6, 11))

x = filter(lambda e: e % 2 == 0, range(5))

from functools import reduce

x = reduce(lambda acc, e: acc - e, range(5))


# itertools

import itertools

counter = itertools.count(1)
for e in counter:
    print(e)
    if e == 5:
        break


count = 1
cycler = itertools.cycle(range(0, 3))
for e in cycler:
    print(e)
    if count == 10:
        break
    count += 1


repeater = itertools.repeat("foo", 3)
for e in repeater:
    print(e)


takewhile = itertools.takewhile(lambda e: e < 10, range(0, 5))
for e in takewhile:
    print(e)


for e in itertools.chain(range(0, 3), range(3, 6)):
    print(e)

for k, g in itertools.groupby("foobar"):
    print(k, list(g))

for k, g in itertools.groupby([1, 2, 2, 1]):
    print(k, list(g))


# find in batch

x = list(range(11))
offset = 0
batch_size = 2
while offset < len(x):
    print(x[offset : offset + batch_size])
    offset += batch_size

x = list(range(11))
for offset in range(0, len(x), batch_size):
    print(x[offset : offset + batch_size])
