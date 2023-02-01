#xor encryption python3
import codecs

text=input("Enter text: ")
key=input("Enter key: ")
#n=len(text)

quote_h  = text
quote_a  = codecs.decode(quote_h, 'hex').decode("utf8")
quote    = quote_a.replace(';', '\n- ')
arr = list(quote)

n=len(arr)
print(arr)
cipher=""
for i in range(n):
    t=arr[i]
    k=key[i%len(key)]
    x=ord(k)^ord(t)
    cipher+=chr(x)
    pass


print(text)
print(key)
print(cipher)



