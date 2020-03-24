import time
import csv
from Crypto.PublicKey import ECC, DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA512

def DSA_1024(data):
	times = []

	key = DSA.generate(1024)
	h = SHA512.new(data)

	controler = DSS.new(key, 'fips-186-3')
	
	start = time.clock()
	signature = controler.sign(h)
	end = time.clock()

	print(signature.hex())
	times.append(end - start)

	start = time.clock()
	verified = controler.verify(h, signature)
	end = time.clock()

	if verified == False: print('authentic message')
	else: print('not authentic message')
	times.append(end - start)

	return times

def ECDSA_521(data):
	times = []

	key = ECC.generate(curve = 'P-521')
	h = SHA512.new(data)

	controler = DSS.new(key, 'fips-186-3')

	start = time.clock()
	signature = controler.sign(h)
	end = time.clock()

	print(signature.hex())
	times.append(end - start)

	start = time.clock()
	verified = controler.verify(h, signature)
	end = time.clock()

	if verified == False: print('authentic message')
	else: print('not authentic message')
	times.append(end - start)

	return times

with open('messages.txt', 'r') as file, open('timesDSA_ECDSA.csv', 'w') as results:
	writer = csv.writer(results, quoting=csv.QUOTE_ALL)
	writer.writerow(['DSA signing', 'DSA verifing', 'ECDSA signing', 'ECDSA verifing'])

	for line in file:
		
		line = line.replace('"','').replace('\n','')
		
		data = line.encode('utf-8')

		print('\nDSA')
		time_dsa = DSA_1024(data)

		print('\nECDSA')
		time_ecdsa = ECDSA_521(data)

		writer.writerow(time_dsa + time_ecdsa)