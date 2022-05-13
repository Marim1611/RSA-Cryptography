# # receiver module 
# # receiver will compute his private key "d" using its public key "e"
# # receiver will send its public key "e" and "n" to the sender
# # receiver will decrypt the cipher text coming from the sender to get the message
import common_functions as cf
import math

class Receiver:
    p=0,
    q=0,
    e=0,
    phi_n=0,
    d=0
    def compute_private_key(self):
        self.phi_n=(self.p-1)*(self.q-1)
        # solve: d = e^-1 mod(phi(n)) => (1/e) * d = x mod(phi(n))
        x=1 # x initially 1
        while x % self.e != 0:
            x +=  self.phi_n
        self.d =   x/self.e
        # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        # print(self.d)
        
        
    def send_public_key(self):
        return self.e

    def decrypt_char(self,C):
        # #decryption: M = C^d mod n
        print("##################")
        print(C)
        print(math.floor(self.d))
        print((self.p * self.q))
        print("##################")
        x=C**math.floor(self.d)
        M = x% (self.p * self.q)
        return M
      
    def decrypt(self,cipher_text):
        print("hello from receiver")
        self.compute_private_key()
        cipher_text_list =list(cipher_text)
        message_list= []
        #print(message_list)
        for character in cipher_text_list:
            # map each character to a number to apply RSA encryption
            character=ord(character) 
            #encrypt each character and store it
            message_list.append(self.decrypt_char(int(character)))
        #convert list to string "the final cipher text"
        print(" receiver cipher list")
        print(cipher_text_list)
        print(message_list)    
        for i in range (0,len(message_list)):
            message_list[i]= chr(message_list[i])
        #print(message_list) 
        message =cf.listToString(message_list)
        #print(message)  
        return message  
# def send_public_key():
      