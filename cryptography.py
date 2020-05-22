# 1 - Cryptographic Hash Functions

import hashlib

def sha256_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

messages = ['Bitcoin', 'Ethereum', 'Cryptocurrency', 'Bitcoin']

for message in messages:
    print('Hash value: ' + sha256_hash(message))
  

# 2 - Public Key cryptography

import hashlib
import rsa

# Secret Message
message = 'Secret message'.encode('utf-8')

# Generate Public and Private keys 256-bits
(publicKey, privateKey) = rsa.newkeys(256)

# Use public Key to encrypt secret message
encrypted_message = rsa.encrypt(message, publicKey)

# Use private Key to decode secret message
decrypted_message = rsa.decrypt(encrypted_message, privateKey)

print(publicKey)
print('\n')
print(privateKey)
print('\n')
print('Encrypted Message: ' + str(encrypted_message))
print('\n')
print('Decrypted Message: ' + decrypted_message.decode('utf-8'))


# 3 - Digital Signatures

import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1

# Generate private and public key
privateKey = SigningKey.generate(curve=SECP256k1)
publicKey = privateKey.verifying_key
print('Private Key: ' + str(privateKey.to_string()))
print('Public Key: ' + str(publicKey.to_string()))
print('\n')


# Hash of a secret message
message = 'Secret message'
print('Original message: ' + message)

def sha256_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()

hash_message = sha256_hash(message)
print('SHA256 Hash Message: ' + hash_message)
print('\n')

# Digital Signature of Hash Message
digital_signature = privateKey.sign(hash_message.encode())
print('Digital Signature: ' + str(digital_signature))
print('\n')

# Verify digital signature
verified = publicKey.verify(digital_signature, hash_message.encode())

if( verified == True):
    print('Message origin verifed by digital signature')
else:
    print('Message not from public/private key pair')
