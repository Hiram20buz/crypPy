#xor encryption python3
import codecs

text=input("Enter text: ")
key=input("Enter key: ")
n=len(text)

cipher=""
for i in range(n):
    t=text[i]
    k=key[i%len(key)]
    x=ord(k)^ord(t)
    cipher+=chr(x)

hexlify = codecs.getencoder('hex')
print(text)
print(key)

#print(cipher.encode("ascii"))
a=hexlify(cipher.encode("ascii"))[0].decode()
print(a)