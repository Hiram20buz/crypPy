# crypPy
Cryptography algorithms

## Xor encryption
### The first thing you need to know is about the xor operation...
### h ^ a
### h => 01101000 in binary , 68 in HEX
### a => 01100001 in binary ,61 in HEX
### 01101000 ^ 01100001=00001001, 68 ^ 61=9
### The problem is that 00001001 does not return any text value.
### To encrypt text you apply the xor operation in all the letters in the file text...
### with a corresponding key,theoretically if the key is as long as the  message is impossible ...
### to decrypt the message.

## Encrypt 
### message:hola
### key:qrs
### h^q,o^r,l^s,a^q
### 68^71, 6F^72, 6C^73, 61^71
### 19 1d 1f 10

## Decrypt 
### message:19 1d 1f 10
### key:qrs
### 19^71, 1d^72, 1f^73, 10^71
### 68 6f 6c 61
### hex to ascci or text
### hola


