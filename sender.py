# SENDER MODULE 
# get the public key of the receiver e & n
# send the message encrypted using RSA algorithm

import senderClass
import socket
import common_functions as cf

my_sender= senderClass.Sender() 
 
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=7634
s.connect((host,port))

# receive the public key from the sender
j=0
p=0
q=0
e=0
while j < 3:
    s_messg=s.recv(1024)
    if j == 0:
        p =int (s_messg)
    if j == 1:
        q = int(s_messg)
    if j == 2:
        e= int(s_messg)       
    j+=1
    
# set public key
my_sender.set_public_key(p,q,e)    

while True:
    message=input("-> ")
    allowed,max=cf.is_key_enough(p*q ,message)
    while not allowed:
        print("~~max allowed length of message is only ",max-1 )
        message=input("-> ")
        allowed,max=cf.is_key_enough(p*q ,message)
    cipher_text= my_sender.encrypt(message)
    s.send(cipher_text.encode())     