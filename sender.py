# SENDER MODULE 
# get the public key of the receiver e & n
# send the message encrypted using RSA algorithm

from email import message


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
    def listToString(self,s): 
        # initialize an empty string
        str1 = "" 
        # traverse in the string  
        for ele in s: 
            print("gg")
            print(ele)
            str1 += ele  
        
        # return string  
        return str1 
     
    def encrypt_char(self,M):
        #check that p and q are primes
        # if not(isPrime(p) and isPrime(q)):
        #     print("p and q must be primes")
        #     return
        n =self.p*self.q
        x=M**self.e
        C=x %n
        return C
         

    def encrypt(self,message):
        print("hello from encrypt")
        message_list =list(message)
        cipher_text_list= []
        #print(message_list)
        for character in message_list:
            # map each character to a number to apply RSA encryption
            character=ord(character) 
            # encrypt each character and store it
            cipher_text_list.append(self.encrypt_char(int(character)))
        #convert list to string "the final cipher text"
        print(cipher_text_list)    
        for i in range (0,len(cipher_text_list)):
            cipher_text_list[i]= chr(cipher_text_list[i])
        print(cipher_text_list) 
        cipher_text =self.listToString(cipher_text_list)
        print(cipher_text)  
        return cipher_text 
            
         
