import os
def encrypt(plain, k):
    str_list = list(plain.lower())
    result = []
    i = 0
    while i < len(str_list):
        if str_list[i] == ' ':
            result.append(' ')
        elif ord(str_list[i]) < 123-k:
            result.append(chr(ord(str_list[i]) + k))
        else:
            result.append(chr(ord(str_list[i]) + k - 26))
        i = i+1
    print ("encrypted："+"".join(result))

def decrypt(cipher, k):
    str_list = list(cipher.lower())
    result = []
    i = 0
    while i < len(str_list):
        if str_list[i] == ' ':
            result.append(' ')
        elif ord(str_list[i]) >= 97+k:
            result.append(chr(ord(str_list[i]) - k))
        else:
            result.append(chr(ord(str_list[i]) + 26 - k))
        i = i+1
    print ("decrypted："+"".join(result))


text = input("Text：")
k = int(input("k："))
k = k % 26
encrypt(text, k)
decrypt(text, k)
