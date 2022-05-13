def listToString(s): 
        # initialize an empty string
        str1 = "" 
        # traverse in the string  
        for ele in s: 
            str1 += ele  
        
        # return string  
        return str1 
# Python program to check if given number is prime or not
def isPrime(num):  
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):

            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False
def gcd(a, b):
    if (a == 0 or b == 0): return 0
     
    # base case
    if (a == b): return a
     
    # a is greater
    if (a > b):
        return gcd(a - b, b)         
    return gcd(a, b - a)

# two numbers are co-prime or not
def areCoprime(a, b):  
    if (gcd(a, b) == 1):
        return True
    else:
        return False           