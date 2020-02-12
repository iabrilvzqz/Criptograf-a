""" Author : Ilse Abril Vazquez Sanchez
	Date : February 11, 2020 """

import fileinput

# This function gets the indices of the given item (character) on the tableau
def getIndexFromTableau(item, tableau):
	for ind in range(len(tableau)):
		if item in tableau[ind]:
			return [ind, tableau[ind].index(item)]

# This function gets the indices on the tableau of the given item (character) 
def getItemFromTableau(i, j, tableau):
	return tableau[i][j]

# This function encrypts a message using the Bifid algorithm
# It receives de clear message and a tableau
def encrypt(message, tableau):
	li, lj = [], []

	# Gets indices of every character of the message
	# Saves all i's in li and all j's in lj
	for c in message:
		index = getIndexFromTableau(c, tableau)
		li.append(index[0])
		lj.append(index[1])

	# Save all j's indices at the end of i's indices
	li += lj

	# With the final list, gets the encrypted message taking pairs of indices
	eMessage = ""
	for i in range(0, len(li), 2):
		eMessage += getItemFromTableau(li[i], li[i+1], tableau)

	return eMessage

# This function decrypts a encrypted message
# It receives an encrypted message (it must be encrypted with Bifid algorithm) and the tableau used to encrypt that message
def decrypt(message, tableau):
	l = []

	# Gets indices of every character of the message
	for c in message:
		l += (getIndexFromTableau(c, tableau))

	# Splits list into two lists in order to obtain the new indices
	l1, l2 = l[0:len(l)//2], l[len(l)//2:]

	# Gets decrypted message iterating over both lists simultaneously
	dMessage = ""
	for i, j in zip(l1, l2):
		dMessage += getItemFromTableau(i, j, tableau)

	return dMessage

def Main():
	# Tableau defined in class with key = 'ENCRYPT'
	tableau = [ ['E', 'N', 'C', 'R', 'Y'], ['P', 'T', 'A', 'B', 'D'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'O', 'Q', 'S'], ['U', 'V', 'W', 'X', 'Z'] ] 

	# Reading file's content
	lines = []
	for line in fileinput.input():
		lines.append(line.replace('\n', "").replace(" ", ""))

	# Chooses between the encrypt and decrypt functions depending on the first line of the file
	if lines[0] == 'ENCRYPT':
		print(encrypt(lines[1], tableau))

	else:
		print(decrypt(lines[1], tableau))

Main()