{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hash value: b4056df6691f8dc72e56302ddad345d65fead3ead9299609a826e2344eb63aa4\n",
      "Hash value: a13bebeb57e1ea699bd4d2d9ac7e58399644e884b8a8783d96f6d146083f2430\n",
      "Hash value: 6ec60fe39028887e7fe9c4b025545748953c27515073bf9ad17ceb5417a407d7\n",
      "Hash value: b4056df6691f8dc72e56302ddad345d65fead3ead9299609a826e2344eb63aa4\n"
     ]
    }
   ],
   "source": [
    "# 1 - Cryptographic Hash Functions\n",
    "\n",
    "import hashlib\n",
    "\n",
    "def sha256_hash(message):\n",
    "    return hashlib.sha256(message.encode()).hexdigest()\n",
    "\n",
    "messages = ['Bitcoin', 'Ethereum', 'Cryptocurrency', 'Bitcoin']\n",
    "\n",
    "for message in messages:\n",
    "    print('Hash value: ' + sha256_hash(message))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PublicKey(66967941732747401577197977802602547770334160247842752577243580637868377822609, 65537)\n",
      "\n",
      "\n",
      "PrivateKey(66967941732747401577197977802602547770334160247842752577243580637868377822609, 65537, 6853441341555713907842391887362181478518668558799497347997798944862957146113, 50386807413967370884033424913078373966481, 1329076898692011425192335870423941889)\n",
      "\n",
      "\n",
      "Encrypted Message: b'~\\xdd\\x8br\\x05\\x9d.\\xb1\\xe2\\x95\\\\\\xbe\\x94U\\x17{\\xfdTb\\x87\\xfb0\\x7f\\xab\\xb5z\\xca\\xa1{K(\\xc6'\n",
      "\n",
      "\n",
      "Decrypted Message: Secret message\n"
     ]
    }
   ],
   "source": [
    "import hashlib\n",
    "import rsa\n",
    "\n",
    "# Secret Message\n",
    "message = 'Secret message'.encode('utf-8')\n",
    "\n",
    "# Generate Public and Private keys 256-bits\n",
    "(publicKey, privateKey) = rsa.newkeys(256)\n",
    "\n",
    "# Use public Key to encrypt secret message\n",
    "encrypted_message = rsa.encrypt(message, publicKey)\n",
    "\n",
    "# Use private Key to decode secret message\n",
    "decrypted_message = rsa.decrypt(encrypted_message, privateKey)\n",
    "\n",
    "print(publicKey)\n",
    "print('\\n')\n",
    "print(privateKey)\n",
    "print('\\n')\n",
    "print('Encrypted Message: ' + str(encrypted_message))\n",
    "print('\\n')\n",
    "print('Decrypted Message: ' + decrypted_message.decode('utf-8'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
