import math as math
import common_functions as cf
import receiverClass as r
import senderClass as s


def mathematical_attack(cipher, n, e):
    decipheredtext = ''
    myReceiver = r.Receiver()
    for p in range(2, int(math.sqrt(n)+1)):
        if(n % p == 0):
            myReceiver.q = n//p
            myReceiver.e = e
            myReceiver.p = p
            decipheredtext = myReceiver.decrypt(cipher)
    return decipheredtext


p = 11
q = 13
modulo = p*q
exponent = cf.generate_e(120)

mySender = s.Sender()
mySender.p = p
mySender.q = q
mySender.e = exponent

ciphertext = mySender.encrypt("attack")
print(mathematical_attack(ciphertext, modulo, exponent))
