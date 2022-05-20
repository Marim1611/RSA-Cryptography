import random
import common_functions as cf
import senderClass as s
import time
import matplotlib.pyplot as plt
#--- 64 => 20 digits
#

theSender= s.Sender()
n= 64
key_lengths=[]
encryption_time=[]
message="hello"
test_file = open("P_Q.txt", "r")
lines = test_file.read().splitlines()
i =0
while i < len(lines)-1:
    # read the message and the public key
    p=int(lines[i])
    q=int(lines[i+1])
    key_lengths.append(len(bin(p*q).replace("0b", "")))
    i+=3
    e= cf.generate_e( (p-1) * (q-1)) 
    print("E")   
    print(e)
    theSender.set_public_key(p,q,e)
    start_time=time.time()
    cipher_text=theSender.encrypt(message) 
    end_time=time.time()
    print(cipher_text)
    encryption_time.append( end_time - start_time)
test_file.close() # close the file   
print(encryption_time)
print(key_lengths)
# plotting the key length VS encryption time (efficiency)
plt.plot(key_lengths,encryption_time )
plt.xlabel('key length in bits')
plt.ylabel('encryption time')
# # giving a title to my graph
plt.title('RSA efficiency')
plt.show()
    


