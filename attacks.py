import common_functions as cf
import receiverClass as r
import senderClass as s

msg=input("enter message")
type= input("MA or CCA ?")
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
C=cf.ConvertToInt(cipher_text)

#write data in file that attacker will intercept
with open('attack_test.txt', 'w') as f:
    f.write(str(C)+ "\n")
    f.write(str(Bob.e) + "\n")
    f.write(str(Bob.p*Bob.q))
f.close()    

#------------------------------ CCA ATTACK -----------------
# Alice to Bob: M ====> C
#interested in finding M given C,e,n
# Eve intercepts C 
if (type == "CCA"):
    attacker_data = open("attack_test.txt", "r")
    lines = attacker_data.read().splitlines()
    i =0
    while i < len(lines)-1:
        C=int(lines[i])
        e=int(lines[i+1])
        n=int(lines[i+2])
        i+=4
    attacker_data.close()
    #intercepted cipher text
    # generate r that is co-prime with el n
    r = cf.generate_e(n) 
    C_dash=C* cf.PowMod( r,e,n)
    # Bob decrypt C dash 
    Y = cf.ConvertToInt( Bob.decrypt( cf.ConvertToStr( C_dash)))
    M= cf.PowMod( (Y* cf.modInverse(r,n)),1,n)
    recovered= cf.ConvertToStr(M)
    #write attack results and original message
    with open('CCA_results.txt', 'w') as f:
        f.write(msg+ "\n")
        f.write(recovered + "\n")
        f.close()
#--------------------- Mathematical Attack ----------------------------------------  
elif (type == "MA"):
    pass
else:
    print("please choose CCA or MA")
 
    






 
    



    