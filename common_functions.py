import random

from numpy import true_divide
def listToString(L): 
        text = "" 
        # traverse in the string  
        for char in L: 
            text += char  
        # return string  
        return text 
def isPrime(n): 
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
def gcd(A, B):
    #base case
    if B == 0:
        return A
    #recursive till b equals to 0    
    return gcd(B, A%B)    
def are_coprimes(A, B):  
    if (gcd(A, B) == 1):
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
# x^y mod n
def power_mod_solve(x, y, n):
    if y == 0:
        return 1 % n
    elif y == 1:
        return x % n
    else:
        b = power_mod_solve(x, y // 2, n)
        b = b * b % n
    if y % 2 == 0:
        return b
    else:
        return b * x % n 

def extended_euclidean_algo(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclidean_algo(b, a % b)
    k = a // b
    return (y, x - k * y)
# b = a^-1 mod n              
def mod_inverse_solve(a, n):
    (b, x) = extended_euclidean_algo(a, n)
    if b < 0:
        b = (b % n + n) % n # get rid of -ve numbers
    return b   

def generate_e(phi_n): 
    # generate e such that it is co-prime with phi n
    e = random.randint(1,phi_n) 
    while not are_coprimes(e, phi_n):
       e = random.randint(1,phi_n)
    return e   

def is_key_enough(n ,msg):
    max_allowed_length= 0
    # char is 8 bits (1 byte) so 2^8 =  256 to know how many char we can encrypt using certain key
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