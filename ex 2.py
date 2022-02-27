import math
import random


def generate_primes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    return [p for p in range(n+1) if prime[p]]

prime_list = generate_primes(100)

p = prime_list[random.randint(0, len(prime_list) - 1)]
q = prime_list[random.randint(0, len(prime_list) - 1)]

# p = 47
# q = 59
n = p * q
totient = (p - 1)*(q - 1)           #Euler function
def gcd(x, y):
    if (y == 0):
        return x
    return gcd(y, x % y)

coprime_list = []
for i in range(n):        #nr are relatively prime if gcd == 1
    if gcd(totient, i) == 1:
        coprime_list.append(i)

random_index = random.randint(0, len(coprime_list) - 1)
d = coprime_list[random_index]
# d = 157

def modInverse(d, totient):
    for e in range(1, totient - 1):
        if (d * e) % totient == 1:
            return e
    return -1
e = modInverse(d, totient)
# print(e)

print(f"d = {d}, e = {e}, p = {p}, q = {q}, totient = {totient}")

text = input("enter a string to convert into ascii values: ")
ascii_values = [ord(character) for character in text]
print(ascii_values)

def encryption(ascii_values):
    encrypted = []
    for i in ascii_values:
        enc = pow(i, e) % n
        encrypted.append(enc)
    return encrypted
encrypted_str = encryption(ascii_values)
print(encrypted_str)

def decryption(encrypted_str):
    decrypted = []
    for i in encrypted_str:
        dec = pow(i, d) % n
        decrypted.append(dec)
    return decrypted
decrypted_str = decryption(encrypted_str)
print(decrypted_str)

from_ascii_values = "".join([chr(value) for value in decrypted_str])
print(from_ascii_values)
