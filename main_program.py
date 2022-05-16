# main program for communication between sender and receiver

import common_functions as cf
import sender
import receiver
import time
import matplotlib.pyplot as plt
#--------------------- the two communicating parties ----------------------
my_sender=sender.Sender()
my_receiver= receiver.Receiver()
#--------------------- Reading the test cases ---------------------------------
test_file = open("test_cases.txt", "r")
lines = test_file.read().splitlines()
i =0
encryption_time=[]
key_length=[]
while i < len(lines)-1:
    print("@@@@@@@@@@@@@@@@@@@@@@@@@ ")
    # read the message and the public key
    p=int(lines[i])
    q=int(lines[i+1])
    message=lines[i+2]
    print("----------- original message --------------")
    print(message)
    e= cf.generate_e( (p-1) * (q-1))
    i+=3
    # check that p and q are primes
    # if not(cf.isPrime(p) and cf.isPrime(q)):
    #     print(" p and q must be primes")
    #     exit()
    #set values of the public key
    my_receiver.p=p
    my_receiver.q=q
    my_receiver.e=e
    # receiver sends its public key to the sender
    my_sender.set_public_key(p,q,e)
    #send the message to the sender to encrypt it
    start_time=time.time()
    cipher_text= my_sender.encrypt(message)
    end_time=time.time()
    encryption_time.append(end_time- start_time)
    key_length.append(len(bin(p*q).replace("0b", "")))
    print("------------------ cipher text ----------------")
    print(cipher_text)
    # send the cipher text to the receiver 
    decrypted_message= my_receiver.decrypt(cipher_text)
    print("------------------ decrypted message ----------------")
    print(decrypted_message)
    print("~~~~~~~~~~~~~~~~~~~~ encryption time: " ,end_time-start_time)
    print("~~~~~~~~~~~~~~~~~~~~ key length: " ,len(bin(p*q).replace("0b", "")))
    print("________________________________________________________________")
# print(encryption_time)
# print(key_length)    
test_file.close() # close the file
# plotting the key length VS encryption time (efficiency)
plt.plot(encryption_time, key_length)
plt.xlabel('encryption time')
plt.ylabel('key length in bits')
# # giving a title to my graph
# plt.title('My first graph!')
#plt.show()
 