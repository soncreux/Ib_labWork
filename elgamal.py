def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots

def primeNums(a, n):
    lst = []
    for i in range(a, n):
        flag = True
        for j in range (2,i):
            if i % j == 0:
                flag = False
        if flag == True: lst.append(i)
    return (lst)

def genP():
    primes = primeNums(500, 1000) # диапозон в котором ищутся простые числа
    random_index = random.randint(0, len(primes) - 1)
    p = primes[random_index]
    return p

def genK(p):
    while True:
        k = random.randint(500, p - 1)
        if k % (p-1) == 0:
            return k

if __name__ == '__main__':
    import random

    message = 499
    p = genP()
    primitiveRoots = primRoots(p)
    randomIndex = random.randint(0, len(primitiveRoots) - 1)
    g = primitiveRoots[randomIndex]
    print("p =", p)
    print("g =", g)
    x = random.randint(1, p-1)
    print("x =", x)
    y = g ** x % p
    print("y =", y)
    k = genK(p)
    print("k =", k)
    a = g ** k % p
    b = y ** k * message % p
    print("a =", a)
    print("b =", b)
    receivedMessage = b * (a ** x) ** (-1) % p
    print("receivedMessage =", receivedMessage)