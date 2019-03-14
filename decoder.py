# -*- coding: utf-8 -*-
from fractions import gcd
import sys

#################################
p = 89
q = 113
n = 89*113
d = 4549
#################################
def int_converter(my_list):
	temp = []
	for i in my_list:
		temp.append(int(i))
	return temp

def decoder(en_list):
	temp=[]
	for i in en_list:
		k = (int(i)**d) % n
		temp.append(k)
	return temp
#################################
f = open('Encrypted.txt', 'r')
en_f = f.read()
a = list(en_f.split(" "))
encrypted = int_converter(a)
decrypted = decoder(encrypted)

print("---------- Checking ---------")
print("p = " + str(p))
print("q = " + str(q))
print("Private Key (n,d) = (" + str(n) + "," + str(d) + ")")
print("---------- Messages ---------")
print("Encrypted: [{}]".format(','.join([str(ee) for ee in encrypted])))
print("Decrypted: [{}]".format(','.join([str(dd) for dd in decrypted])))

print("------- ASCII Convert -------")
char = [chr(dd) for dd in decrypted]
print("Message: {}".format(''.join([cc for cc in char])))
print("----------- End -------------")
