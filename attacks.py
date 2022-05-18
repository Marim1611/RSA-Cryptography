import common_functions as cf
import receiverClass as r
import senderClass as s
msg="hello"
# Bob (receiver) decryption
Bob= r.Receiver()
Bob_data = open("pq.txt", "r")
lines = Bob_data.read().splitlines()
i =0
while i < len(lines)-1:
    Bob.p=int(lines[i])
    Bob.q=int(lines[i+1])
    i+=3
Bob_data.close() 
Bob.e=cf.generate_e( (Bob.p-1) * (Bob.q-1))
e= Bob.e
#Sender: Alice
Alice = s.Sender()
Alice.set_public_key( Bob.p, Bob.q , Bob.e)
cipher_text = Alice.encrypt(msg)

C= Alice.encrypt(msg)
#write data in file that attacker will intercept
with open('attack_test.txt', 'w') as f:
    f.write(C + "\n")
    f.write(str(Bob.e) + "\n")
    f.write(str(Bob.p*Bob.q) + "\n")
f.close()     




 
    



    