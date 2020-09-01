from Crypto.Util.number import getPrime
from random import randrange
from math import gcd


bits = int(input("Enter bit length of the primes: "))

print(f"RSA key generation with {bits} bit primes")

p = getPrime(bits)
q = getPrime(bits)
n = p * q

z = (p - 1) * (q - 1)

print(f"p (prime): {p} q (prime): {q}")
print(f"n: {n}")
print(f"z: {z}")

e = randrange(1, z)

while True:
    e = randrange(1, z)
    if gcd(e, z) == 1 and pow(e, -1, z) != e:
        break

print(f"e (public key): {e}")
d = pow(e, -1, z)
print(f"d (private key): {d}")
