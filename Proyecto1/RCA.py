import time
import csv
import binascii
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

publicKey = None
privateKey = None

def createRCAkeys(n, e, d):
    global privateKey, publicKey

    privateKey = RSA.construct((n, e, d))
    publicKey = privateKey.publickey()

    f = open('publicKey.pem','wb')
    f.write(publicKey.exportKey('PEM'))
    f.close()

    f = open('privateKey.pem','wb')
    f.write(privateKey.exportKey('PEM'))
    f.close()


def RSA_PSS(data):
    hashValue = SHA256.new(data)

    signFunction = pss.new(privateKey)
    signature = signFunction.sign(hashValue)

    print(signature.hex())

    verifier = pss.new(publicKey)
    try:
        verifier.verify(hashValue, signature)
        print("The signature is authentic.")
    except (ValueError, TypeError):
        print("The signature is not authentic.")

def RSA_OAEP(data):
    cipher = PKCS1_OAEP.new(publicKey)

    ciphertext = cipher.encrypt(data)
    print(ciphertext.hex())

    decipher = PKCS1_OAEP.new(privateKey)

    plainText = decipher.decrypt(ciphertext)
    print(plainText.hex())

with open("test.csv") as test_vectors:
    reader = csv.reader(test_vectors, delimiter = ",")
    for row in reader:
        n = int(row[0], 16)
        e = int(row[1], 16)
        d = int(row[2], 16)
        data =  bytes.fromhex(row[3])
        createRCAkeys(n, e, d)
        RSA_OAEP(data)
        RSA_PSS(data)
