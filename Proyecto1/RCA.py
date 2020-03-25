import time
import csv
import binascii
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

def createRCAkeys(n, e, d):
    # n = 0x9195E9854FA04A1433D4E22048951426A0ACFC6FE446730579D742CAEA5FDF6590FAEC7F71F3EBF0C6408564987D07E19EC07BC0F601B5E6ADB28D9AA6148FCC51CFF393178983790CC616C0EF34AB50DC8444F44E24117B46A47FA3630BF7E696865BFC245F7C3A314CD48C583D7B2223AF06881158557E37B3CC370AE6C8D5
    # e = 0x010001
    # d = 0x05B2DDE134ACB6E448E31C618720796EC9A5FBD0FAC3DC876A5832BFC94CD76C725B0AC6DCFF09F7F2CAB3C356F4B89F96F1E73B8BBAFABE7CD8C5BCE2A360BD8A3CE2767A2F83A6B143C2446D5A0388748F91813BB5E7A6CEA402368842DBC50C11EFE6B26CB08B53B83BC7FB17D5A62C39A6CCC718165D59375BE387642601

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

    privateKeyFile = open("./privateKey.pem", "r")
    privateKey = RSA.importKey(privateKeyFile.read())
    signFunction = pss.new(privateKey)
    signature = signFunction.sign(hashValue)

    print(signature.hex())

    publicKeyFile = open("./publicKey.pem", "r")
    publicKey = RSA.importKey(publicKeyFile.read())
    verifier = pss.new(publicKey)

    try:
        verifier.verify(hashValue, signature)
        print("The signature is authentic.")
    except (ValueError, TypeError):
        print("The signature is not authentic.")

def RSA_OAEP(data):
    publicKeyFile = open("./publicKey.pem", "r")
    publicKey = RSA.importKey(publicKeyFile.read())
    cipher = PKCS1_OAEP.new(publicKey)

    ciphertext = cipher.encrypt(data)
    print(ciphertext.hex())

    privateKeyFile = open("./privateKey.pem", "r")
    privateKey = RSA.importKey(privateKeyFile.read())
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


# createRCAkeys()
# data = bytes.fromhex("0000000000000000000000000000000000000000")
# RSA_PSS(data)
# data = bytes.fromhex("8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
# RSA_OAEP(data)
