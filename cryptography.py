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
