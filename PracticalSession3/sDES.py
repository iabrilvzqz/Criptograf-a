""" Author : Ilse Abril Vazquez Sanchez
	Date : February 16, 2020 """

import fileinput

def initialPermutation(plaintext):
	# Changes the order of plaintext
	# This permutation can be expressed as (1,5,2,0,3,7,4,6)
	b = plaintext
	return ("").join([b[1], b[5], b[2], b[0], b[3], b[7], b[4], b[6]])

def inversePermutation(finaltext):
	# Changes the order of the result obtained after two rounds
	# This permutation can be expressed as (3,0,2,4,6,1,7,5)
	b = finaltext
	return ("").join([b[3], b[0], b[2], b[4], b[6], b[1], b[7], b[5]])

def subkeys(key):
	# Simplified DES uses a 10-bit key
	# Obtaines two 8-bit subkeys for each round with the following permutations
	# k1 = (0,6,8,3,7,2,9,5)
	# k2 = (7,2,5,4,9,1,8,0) 
	k = key
	k1 = [k[0], k[6], k[8], k[3], k[7], k[2], k[9], k[5]]
	k2 = [k[7], k[2], k[5], k[4], k[9], k[1], k[8], k[0]]

	return [("").join(k1), ("").join(k2)]

def mixingFunction(subkey, block):

	#S-boxes
	S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
	S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

	# The 4-bit block is expanded into 8-bits
	expandedBlock = [block[3], block[0], block[1], block[2], block[1], block[2], block[3], block[0] ]

	# The subkey is XOR-ed with the expanded block
	firstXOR = [ int(a) ^ int(b) for a, b in zip(subkey, expandedBlock)]

	# Bits 0+3 and 1+2 are used as input to S0; bits 4+7 and 5+6 as input for S1
	i, j = int( str(firstXOR[0]) + str(firstXOR[3]), 2), int( str(firstXOR[1]) + str(firstXOR[2]), 2)

	k, l = int( str(firstXOR[4]) + str(firstXOR[7]), 2), int( str(firstXOR[5]) + str(firstXOR[6]), 2)

	x = [ S0[i][j], S1[k][l]]
	
	# The outputs of S0 and S1 are converted to its binary value, concatenated and permuted
	x = ("").join( ["{:02b}".format(a) for a in x] )
	x = list(x)

	x[0], x[1], x[2], x[3] = x[1], x[3], x[2], x[0]

	return ("").join(x)
	

def Main():
	# Reading file's content
	lines = []
	for line in fileinput.input():
		lines.append(line.replace('\n', ""))

	# Initial permutation
	c = initialPermutation(lines[2])

	# Generate subkeys
	keys = subkeys(lines[1])

	# For decryption we first use k2 and then k1
	if lines[0] == 'D':
		keys[0], keys[1] = keys[1], keys[0]

	# Feistel operation using subkey 1
	x = mixingFunction(keys[0], c[4:])
	secondXOR = [ str( int(a) ^ int(b) ) for a, b in zip(c[0:4], x)]

	# Switch left and right halves
	c = c[4:] + ("").join(secondXOR)

	# Feistel operation using subkey 2
	x = mixingFunction(keys[1], c[4:])
	thirdXOR = [ str( int(a) ^ int(b) ) for a, b in zip(c[0:4], x)]
	
	# Concatenate left and right halves
	c = ("").join(thirdXOR) + c[4:]

	# Inverse permutation
	print(inversePermutation(c))

Main()
