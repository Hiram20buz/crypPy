#xor encryption python3
import codecs

filex=input("Enter file: ")
#
# opening the original file to encrypt
with open(filex, 'rb') as file:
    original = file.read()
     

key=input("Enter key: ")


cipher=""
i=0
for line in original:
    t=chr(line)
    k=key[i%len(key)]
    x=ord(k)^ord(t)
    cipher+=chr(x)
    i+=1


with open(filex, 'wb') as encrypted_file:
    hexlify = codecs.getencoder('hex')
    #a=hexlify(cipher.encode("ascii"))[0].decode()
    a=hexlify(cipher.encode("ascii"))[0]
    encrypted_file.write(a)



