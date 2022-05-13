# main program for communication between sender and receiver
import common_functions as cf
import sender
import receiver

my_sender=sender.Sender()
my_receiver= receiver.Receiver()
test_file = open("test_p_q_e.txt", "r")
i =0
p=283
q=439
e=521
#check that p and q are primes
if not(cf.isPrime(p) and cf.isPrime(q)):
    print(" p and q must be primes")
    exit()
#check that phi(n) and e are co-primes
if not(cf.areCoprime((p-1)*(q-1) ,e)):
    print(" e and phi of n are not co-prime")
    exit()    
#set values of the public key
my_receiver.p=p
my_receiver.q=q
my_receiver.e=e
# receiver sends the public key to the sender
my_sender.set_public_key(p,q,e)
# read the message & send it to the sender to encrypt it
message="Marioma KEEP GOING ! <3 133"
cipher_text= my_sender.encrypt(message)
print("****************")
print(cipher_text)
# send the cipher text to the receiver 
decrypted_message= my_receiver.decrypt(cipher_text)
print("**** the end****")
print(decrypted_message)



#

# for line in test_file:
#     p= line[0]
#     q=line [2] 
# print(p)
# print(q)       
         

 
# message = input("Enter the message: ")
# print(message)
# sender.encrypt(message)