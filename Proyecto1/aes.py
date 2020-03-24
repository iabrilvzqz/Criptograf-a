
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

def AES_ECB(key, data):
	cipher = AES.new(key, AES.MODE_ECB)

	ct = cipher.encrypt(pad(data, AES.block_size))
	print(ct.hex())

	pt = unpad(cipher.decrypt(ct), AES.block_size)
	print('Pt', pt)


def  AES_CBC(key, data):
	
	cipher = AES.new(key, AES.MODE_CBC)

	ct = cipher.encrypt(pad(data, AES.block_size))
	print(ct.hex())

	decipher = AES.new(key, AES.MODE_CBC, cipher.iv)

	pt = unpad(decipher.decrypt(ct), AES.block_size)
	print('Pt', pt)


key = b"80000000000000000000000000000000"
data = b"abcdefghijklmnopqrstuvwxyz"
print("AES ECB")
AES_ECB(key, data)
print("\nAES CBC")
AES_CBC(key, data)
"""
aes_ec_code = "aes_ebc.encrypt(Padding.pad(inputBits, 16))"
aes_dc_code = "aes_ebc.decrypt(ct)"

aes_ec_time = timeit.timeit(setup=aes_setup, stmt=aes_ec_code, number=100)
aes_dc_time = timeit.timeit(setup=aes_setup, stmt=aes_dc_code, number=100)

print(aes_ec_time)
print(aes_dc_time)"""