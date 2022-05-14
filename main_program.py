# main program for communication between sender and receiver

import common_functions as cf
import sender
import receiver
#--------------------- the two communicating parties ----------------------
my_sender=sender.Sender()
my_receiver= receiver.Receiver()
#--------------------- Reading the test cases ---------------------------------
test_file = open("test_cases.txt", "r")
lines = test_file.read().splitlines()
i =0
while i < len(lines):
    # read the message and the public key
    p=int(lines[i])
    q=int(lines[i+1])
    e=int(lines[i+2])
    message=lines[i+3]
    i+=4
    print("----------- original message --------------")
    print(message)
    # check that p and q are primes
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
    # receiver sends its public key to the sender
    my_sender.set_public_key(p,q,e)
    #send the message to the sender to encrypt it
    cipher_text= my_sender.encrypt(message)
    print("------------------ cipher text ----------------")
    print(cipher_text)
    # send the cipher text to the receiver 
    decrypted_message= my_receiver.decrypt(cipher_text)
    print("------------------ decrypted message ----------------")
    print(decrypted_message)
    print("________________________________________________________________")
test_file.close() # close the file
 