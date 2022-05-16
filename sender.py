# SENDER MODULE 
# get the public key of the receiver e & n
# send the message encrypted using RSA algorithm

import common_functions as cf

class Sender:
    #public key
    p=0,
    q=0,
    e=0, 
    # functions
    def set_public_key(self,P,Q,E):
        self.p=P
        self.q=Q
        self.e=E

    def encrypt(self,message):
        # the msg a number to apply RSA encryption
        M=cf.ConvertToInt(message) 
        C=cf.PowMod(M, self.e , self.p * self.q)
        cipher_text=cf.ConvertToStr(C)
        return cipher_text
