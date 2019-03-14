# -*- coding: utf-8 -*-
from fractions import gcd
import sys

p = 89
q = 113
n = 89*113
psi = (p-1)*(q-1)
e = 5
##################################
def int_converter(my_list):
	temp = []
	for i in my_list:
		temp.append(int(i))
	return temp

def str_converter(my_list):
	temp = ""; last=my_list.pop()
	for i in my_list:
		temp = temp + str(i) + " "
	temp = temp + str(last)
	return temp

def decoder(en_list):
	temp=[]
	for i in en_list:
		k = (int(i)**d) % n
		temp.append(k)
	return temp

def encoder(en_list):
	temp=[]
	for i in en_list:
		k = (int(i)**e) % n
		temp.append(k)
	return temp
##################################
messsage = "I am david halladay"
plain = [ord(mm) for mm in messsage]
d = 17741
plain_int = int_converter(plain)
encrypted = encoder(plain_int)
decrypted = decoder(encrypted)

f = open('My_Encrypt.txt','w')
f.write(str_converter(encrypted))

##################################
# how I find the unknowed 'd'
# ed ≡ 1 (mod psi) from the RSA encrypted
# 5d ≡ 1 (mod 9856)
# 5d-1 = 9856*m (m is a constant)
# we find m = 9 (minimum answer)
# d = 17741
##################################

print("---------- Checking ---------")
print("p = " + str(p))
print("q = " + str(q))
print("Public Key  (n,e) = (" + str(n) + "," + str(e) + ")")
print("Private Key (n,d) = (" + str(n) + "," + str(d) + ")")
print("---------- Messages ---------")
print("Encrypted: [{}]".format(','.join([str(ee) for ee in encrypted])))
print("Decrypted: [{}]".format(','.join([str(dd) for dd in decrypted])))

print("------- ASCII Convert -------")
char = [chr(dd) for dd in decrypted]
print("Message: {}".format(''.join([cc for cc in char])))
print("----------- End -------------")
