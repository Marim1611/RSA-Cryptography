import common_functions as cf
import receiverClass as r
import senderClass as s

def MA(C, n, e):
    recovered = ''
    Eve = r.Receiver()
    for p in range(2, int((n**0.5)+1)):
        if(n % p == 0):
            Eve.q = n//p
            Eve.e = e
            Eve.p = p
            recovered = Eve.decrypt(cf.ConvertToStr(C))

    return recovered

def CCA(C, n, e):
    
    #intercepted cipher text
    # generate r that is co-prime with el n
    r = cf.generate_e(n) 
    C_dash=C* cf.PowMod( r,e,n)
    # Bob decrypt C dash 
    Y = cf.ConvertToInt( Bob.decrypt( cf.ConvertToStr( C_dash)))
    M= cf.PowMod( (Y* cf.modInverse(r,n)),1,n)
    recovered= cf.ConvertToStr(M)

    return recovered



msg=input("Enter message: ")
type= input("For MA press 1, For CCA press 2: ")

# Alice to Bob: M ====> C
#interested in finding M given C,e,n
# Eve intercepts C 
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


attacker_data = open("attack_test.txt", "r")
lines = attacker_data.read().splitlines()
i =0
while i < len(lines)-1:
    C=int(lines[i])
    e=int(lines[i+1])
    n=int(lines[i+2])
    i+=4
attacker_data.close()

#---------------------------- Mathematical Attack --------------  
if (type == "1"):

    recovered= MA(C, n, e)
    
    #write attack results and original message
    with open('MA_results.txt', 'w') as f:
        f.write("Original message: "+ msg+ "\n")
        f.write("Recovered message: "+ recovered + "\n")
        f.close()

    print("The attack is done, hard luck next time!")


#------------------------------ CCA ATTACK -----------------

elif (type == "2"):
   
    recovered= CCA(C, n, e)

    #write attack results and original message
    with open('CCA_results.txt', 'w') as f:
        f.write("Original message: "+ msg+ "\n")
        f.write("Recovered message: "+ recovered + "\n")
        f.close()

    print("The attack is done, hard luck next time!")

else:
    print("please choose 1 or 2")