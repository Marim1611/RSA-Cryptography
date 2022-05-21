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
def isPrime(n):     return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
# def isPrime(num):  
#     # If given number is greater than 1
#     if num > 1:
#         # Iterate from 2 to n / 2
#         for i in range(2, int(num**0.5)+1):

#             # If num is divisible by any number between
#             # 2 and n / 2, it is not prime
#             if (num % i) == 0:
#                 return False
#                 break
#         else:
#             return True

#     else:
#         return False
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)    
    # if (a == 0 or b == 0): return 0
    # # base case
    # if (a == b): return a
    # # a is greater
    # if (a > b):
    #     return gcd(a % b, b)         
    # return gcd(a, b % a)
# two numbers are co-prime or not
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
def msg_length_available(n ,msg):
    allowed_length=n // 256
    if allowed_length == len(msg):
        return 1
    else:
        return 0    
def is_key_enough(n ,msg):
    max_allowed_length= 0
    while n != 0:
        n= n //256
        max_allowed_length +=1
    print("key length")
    print(len(msg))
    print(max_allowed_length)    
    if len(msg) < max_allowed_length:
        return True , max_allowed_length
    else:
        return False ,max_allowed_length