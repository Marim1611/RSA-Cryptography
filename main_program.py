# main program for communication between sender and receiver
from pip import List
import sender
import receiver

my_sender=sender.Sender()
my_receiver= receiver.Receiver()
test_file = open("test_p_q_e.txt", "r")
i =0
p=11
q=7
e=3
#set values of the public key
my_receiver.p=p
my_receiver.q=q
my_receiver.e=e
# receiver sends the public key to the sender
my_sender.set_public_key(p,q,e)
# read the message & send it to the sender to encrypt it
message="hello i am marim!"
my_sender.encrypt(message)


#

# for line in test_file:
#     p= line[0]
#     q=line [2] 
# print(p)
# print(q)       
         

 
# message = input("Enter the message: ")
# print(message)
# sender.encrypt(message)