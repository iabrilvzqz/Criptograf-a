import hashlib

with open("messages.txt", 'r') as file:

	for line in file:

		line = line.replace("\"\"", "").replace("\n", "")

		message = line.encode()

		SHA1 = hashlib.sha1(message).hexdigest()
		SHA256 = hashlib.sha256(message).hexdigest()
		SHA3 =  hashlib.sha3_256(message).hexdigest()

		print("\nMensaje: " + line)
		print("SHA1: " + SHA1)
		print("SHA2: "+ SHA256)
		print("SHA3-256: " + SHA3)