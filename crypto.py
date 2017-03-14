import math
import random


def invmodp(a, p):
    '''
    The multiplicitive inverse of a in the integers modulo p.
    Return b s.t.
    a * b == 1 mod p
    '''

    for d in range(1, p):
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d


def create_pool():
    count = 31
    pool = []
    while count < 450:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            pool.append(count)

        count += 1
    return pool

pool = create_pool()

p = random.choice(pool)
q = random.choice(pool)

n = p * q

phi_n = (p-1) * (q-1)

e = 1

while e <= 1 or e >= phi_n or math.gcd(e, phi_n) != 1:
    e = int(random.random()*phi_n)

d = invmodp(e, phi_n)

print("private({}, {})".format(d, n))
print("public({}, {})".format(e, n))
