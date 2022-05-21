# # receiver module 
# # receiver will compute his private key "d" using its public key "e"
# # receiver will send its public key "e" and "n" to the sender
# # receiver will decrypt the cipher text coming from the sender to get the message

import common_functions as cf
import receiverClass
import socket
#----------------------------- 
my_receiver= receiverClass.Receiver()
test_file = open("test_cases.txt", "r")
lines = test_file.read().splitlines()
i =0
while i < len(lines)-1:
    # read the message and the public key
    p=int(lines[i])
    q=int(lines[i+1])
    i+=3
test_file.close() # close the file   

#generate public key e if not given  
# if e == "" or e == " ":
#    print("e is not  given")
e= cf.generate_e( (p-1) * (q-1))


        
# check that p and q are primes
    # if not(cf.isPrime(p) and cf.isPrime(q)):
    #     print(" p and q must be primes")
    #     exit()
  
#set values of the public key
my_receiver.p=p
my_receiver.q=q
my_receiver.e=e
#communication:
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=7634
s.bind((host,port))
s.listen(1)
con,addr=s.accept()
print("connected with",addr)
publick_key=[p ,q,e]
# receiver sends its public key to the sender
j=0
while j < 3:
    messg=str(publick_key[j])
    con.send(messg.encode())
    j+=1

while True:
    cipher_text=con.recv(1024)
    cipher_text=cipher_text.decode()
    print("cipher text received: ",cipher_text)
    decrypted_message= my_receiver.decrypt(cipher_text)
    print("original message from sender: ",decrypted_message)
    print('\n')
       

        
     
      