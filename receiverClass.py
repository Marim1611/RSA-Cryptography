import common_functions as cf
import math
import socket
class Receiver:
    p=0,
    q=0,
    e=0,
    phi_n=0,
    d=0
    def compute_private_key(self):
        self.phi_n=(self.p-1)*(self.q-1)
        #d = e^-1 mod phi(n)
        self.d =cf.mod_inverse_solve( self.e ,   self.phi_n)
        
    def send_public_key(self):
        return self.e
      
    def decrypt(self,cipher_text):
        #receiver compute his private key
        self.compute_private_key()
        C=cf.ConvertToInt(cipher_text)
        # #decryption: M = C^d mod n
        M=cf.power_mod_solve(C, math.floor(self.d) , self.p * self.q)
        decrypted_message=cf.ConvertToStr(M)
        return decrypted_message