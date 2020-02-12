""" Author : Ilse Abril Vazquez Sanchez
	Date : February 18, 2020 """

import fileinput

# Key-scheduling algorithm
def KSA(key):
	# Initialization of S with numbers from 0 to 255
	S = [i for i in range(256)]
	j = 0
	keylength = len(key)

	# S is processed for 255 iterations to mix the bytes of the key
	for i in range(256):
		j = (j + S[i] + key[i % keylength]) % 256
		
		# Swap values of S[i] and S[j]
		temp = S[i]
		S[i] = S[j]
		S[j] = temp

	return S

# Pseudo-random generation algorithm
def PRGA(S):
	i = 0
	j = 0

	while True:
		# Incrementing i to look up the ith element of S
		i = (i + 1) % 256
		# The ith element of S adds to j
		j = (j + S[i]) % 256

		# Swap values of S[i] and S[j]
		temp = S[i]
		S[i] = S[j]
		S[j] = temp

		# Byte of the keystream that will be used to make the xor operation
		k = S [ (S[i] + S[j]) % 256 ]

		# Everytime we need a new byte for the keystream, the PRGA function will restart from this point to return to the beginning of "while" 
		yield k

def RC4(key):
	# Algorithm used to initialize the permutation in the array S
	S = KSA(key)
	return PRGA(S)

def Main():

	# Reading file's content
	lines = []
	for line in fileinput.input():
		lines.append(line.replace('\n', ""))

	# Converts each character of the key and plain text to its ASCII value
	key = [ord(c) for c in lines[0]]
	plaintext = [ord(c) for c in lines[1]]

	# Starts algorithm
	# keystream will be a generator that will contain the result obtained in every iteration in PRGA function
	keystream = RC4(key)

	result = []

	for (c, k) in zip(plaintext, keystream):
		# xor between the characters of the plain text and the elements of the keystream to encrypt the message
		result.append("{:02x}".format(c ^ k))

	print(("".join(result)).upper())

Main()


