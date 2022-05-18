# CCA cipher chosen attack
# Alice to Bob: M ====> C
#interested in finding M given C,e,n
# Eve intercepts C 

import common_functions as cf
import attacks as a
attacker_data = open("attack_test.txt", "r")
lines = attacker_data.read().splitlines()
i =0
while i < len(lines)-1:
    C=int(lines[i])
    e=int(lines[i+1])
    n=int(lines[i+2])
    i+=4
attacker_data.close()
r = cf.generate_e(n) 
C_dash= cf.PowMod(C,r,n)
Y = a.Bob.decrypt(C_dash)
M=Y * (cf.modInverse(r,n) )
print("*******")
print(M)
