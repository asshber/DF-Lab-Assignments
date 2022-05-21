import os
import argparse
from pickletools import optimize
import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from click import Argument

# Public and Private RSA keys can be generated through 'openssl req -new -x509 -newkey rsa:2048 -keyout Privkey.out -pubkey -out Pubkey.out -days 365 -nodes -sha256'
parser=argparse.ArgumentParser()
parser.add_argument('option')
parser.add_argument('device')
arg=parser.parse_args()
if arg.option=="eject":
    device=open(arg.device,'rb')
    contents=device.read()
    h=SHA256.new(contents)
    with open("./Privkey.out", 'rb') as f: key = f.read()
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    with open("/home/ashber/DF-Lab/Assignments/Assignment-02/.signature",'wb') as f: f.write(signature)
elif arg.option=="mount":
    device=open(arg.device,'rb')
    contents=device.read()
    h=SHA256.new(contents)
    with open("/home/ashber/DF-Lab/Assignments/Assignment-02/Pubkey.out", 'rb') as f: key = f.read()
    rsa = RSA.importKey(key)
    signer = PKCS1_v1_5.new(rsa)
    with open("/home/ashber/DF-Lab/Assignments/Assignment-02/.signature",'rb') as f: 
        orig_sign=f.read()
        if signer.verify(h,orig_sign):
            print("Integrity Check passed")
        else:
            print("Integrity Check failed")
