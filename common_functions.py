import random

from numpy import true_divide
def listToString(s): 
        # initialize an empty string
        str1 = "" 
        # traverse in the string  
        for ele in s: 
            str1 += ele  
        # return string  
        return str1 
# Python program to check if given number is prime or not
def isPrime(n): 
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)    
def areCoprime(a, b):  
    if (gcd(a, b) == 1):
        return True
    else:
        return False    
def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]
def ConvertToInt(message_str):
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res
def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
    if n % 2 == 0:
        return b
    else:
        return b * a % mod 

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)
               
def modInverse(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n # we don't want -ve integers
    return b   

def generate_e(phi_n): 
    e = random.randint(1,phi_n) 
    while not areCoprime(e, phi_n):
       e = random.randint(1,phi_n)
    return e   

def is_key_enough(n ,msg):
    max_allowed_length= 0
    while n != 0:
        n= n //256
        max_allowed_length +=1    
    if len(msg) < max_allowed_length:
        return True , max_allowed_length
    else:
        return False ,max_allowed_length

def generate_pq(n):
    p=random.getrandbits(int(n/2))
    q=random.getrandbits(int(n/2))
    while not isPrime(p):
        p=random.getrandbits(int(n/2))
    while not isPrime(q) or p==q:
        q=random.getrandbits(int(n/2))
    return p,q