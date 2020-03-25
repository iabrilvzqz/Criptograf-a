import time
import csv
from Cryptodome.PublicKey import ECC, DSA
from Cryptodome.Signature import DSS
from Cryptodome.Hash import SHA512

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

	try:
		start = time.clock()
		controler.verify(h, signature)
		end = time.clock()
		print('The message is authentic')
	except ValueError:
		print('The message is not authentic')
	
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

	try:
		start = time.clock()
		controler.verify(h, signature)
		end = time.clock()
		print('The message is authentic')
	except ValueError:
		print('The message is not authentic')
	
	times.append(end - start)

	return times

with open('messages2.txt', 'r') as file, open('timesDSA_ECDSA.csv', 'w') as results:
	writer = csv.writer(results, quoting=csv.QUOTE_ALL)
	writer.writerow(['DSA signing', 'DSA verifing', 'ECDSA signing', 'ECDSA verifing'])

	for line in file:
		
		line = line.replace('"','').replace('\n','')
		
		data = bytes.fromhex(line)

		print('\nDSA')
		time_dsa = DSA_1024(data)

		print('\nECDSA')
		time_ecdsa = ECDSA_521(data)

		writer.writerow(time_dsa + time_ecdsa)