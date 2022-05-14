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
     
    def encrypt_char(self,M):
        #check that p and q are primes
        n =self.p*self.q
        x=M**self.e
        C=x %n
        return C
         

    def encrypt(self,message):
        message_list =list(message)
        cipher_text_list= []
        for character in message_list:
            # map each character to a number to apply RSA encryption
            character=ord(character) 
            # encrypt each character and store it
            cipher_text_list.append(self.encrypt_char(int(character)))
        #convert list to string "the final cipher text"   
        for i in range (0,len(cipher_text_list)):
            cipher_text_list[i]= chr(cipher_text_list[i])
        cipher_text =cf.listToString(cipher_text_list) 
        return cipher_text 
            
         
