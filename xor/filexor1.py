#xor encryption python3
import codecs

filex=input("Enter file: ")
#
# opening the original file to encrypt
with open(filex, 'rb') as file:
    original = file.read()
     

key=input("Enter key: ")

my_list = []
cipher=""
#i=1
for line in original:
    z1=chr(line)
    #z2=z1.encode("ascii")
    my_list.append(z1)
    
def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
 
 
# Driver code
text=listToString(my_list).encode("ascii")
print(text)

quote_a  = codecs.decode(text, 'hex').decode("ASCII")
quote    = quote_a.replace(';', '\n- ')
arr = list(quote)

n=len(arr)
print(arr)
    
    
for i in range(n):
    t=arr[i]
    k=key[i%len(key)]
    x=ord(k)^ord(t)
    cipher+=chr(x)
    #i+=1
    #print(z2)
    #print(hex(line))
    #print(cipher)
    #pass

print(cipher.encode("ascii"))
with open(filex, 'wb') as encrypted_file:
    #hexlify = codecs.getencoder('hex')
    #a=hexlify(cipher.encode("ascii"))[0].decode()
    #a=hexlify(cipher.encode("ascii"))[0]
    encrypted_file.write(cipher.encode("ascii"))
    
    