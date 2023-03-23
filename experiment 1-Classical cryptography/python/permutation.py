# 矩阵换位加密与解密
import math
def encrypt(plain, k):
    cipher_list = list(k)
    plain_text_list = list(plain.replace(" ",""))
    # 密钥ASCII码列表
    cipher_ord_list = []
    # 密钥顺序列表，储存每个字母在整个密钥中的排序
    cipher_sort_list = []
    # 密文列表，存放明文加密后的密文
    cipher_text_list = plain_text_list[:]
    # 密钥长度
    cipher_length = len(cipher_list)
    # 明文长度
    plain_text_length = len(plain_text_list)
    # 要补齐的'x'字母数目
    l =len(cipher_list) - len(plain_text_list) % len(cipher_list)
    # 矩阵的行数
    row = math.floor(plain_text_length / cipher_length)
    print("plain matrix:",end="")
    # 不足补abcd...
    a = ord('a')
    for j in range(0,l):
        plain_text_list.append(chr(a))
        a = a+1
    # 输出明文矩阵
    for i in range(0,plain_text_length):
        if i%cipher_length ==0:
            print("")
        print(plain_text_list[i],end="")
    print("\ncipher matrix",end="")
    for i in range(0,cipher_length):
        cipher_ord_list.append(ord(cipher_list[i]))
    for i in range(0,cipher_length):
        sum = 0
        for j in range(0,cipher_length): 
            if cipher_ord_list[i] < cipher_ord_list[j]:
                sum += 1
        cipher_sort_list.append(cipher_length-sum-1)
    # 矩阵换位加密
    for i in range(0,cipher_length):
        for k in range(0,row):
            cipher_text_list[k*cipher_length+i] = \
                plain_text_list[k*cipher_length+cipher_sort_list[i]]
    for i in range(0,plain_text_length):
        if i % cipher_length == 0:
            print("")
        print(cipher_text_list[i], end="")
    cipher = "".join(cipher_text_list)
    return cipher

def decrypt(cipher, k):
    cipher_list = list(k)
    cipher_text_list = list(cipher.replace(" ", ""))
    # 密钥ASCII码列表
    cipher_ord_list = []
    # 密钥顺序列表，储存每个字母在整个密钥中的排序
    cipher_sort_list = []
    # 明文列表，存放密文解密后的明文
    plain_text_list = cipher_text_list[:]
    # 密钥长度
    cipher_length = len(cipher_list)
    # 密文长度
    cipher_text_length = len(cipher_text_list)
    # 矩阵的行数
    row = math.floor(cipher_text_length / cipher_length)
    # 输出密文矩阵  
    print("密文矩阵为：",end="")
    for i in range(0, cipher_text_length):
        if i % cipher_length == 0:
            print("")
        print(cipher_text_list[i], end="")
    print("\n解密后的明文矩阵为", end="")
    for i in range(0, cipher_length):
        cipher_ord_list.append(ord(cipher_list[i]))
    for i in range(0, cipher_length):
        sum = 0
        for j in range(0, cipher_length):
            if cipher_ord_list[i] < cipher_ord_list[j]: 
                sum += 1
        cipher_sort_list.append(cipher_length - sum - 1)
    # 矩阵换位解密
    for i in range(0, cipher_length):
        for k in range(0, row):
            plain_text_list[k * cipher_length + cipher_sort_list[i]] = \
                cipher_text_list[k * cipher_length + i]
    for i in range(0,cipher_text_length):
        if i % cipher_length == 0:
            print("")
        print(plain_text_list[i], end="")
    plain = "".join(plain_text_list)
    return plain

text = input("Text:\n")
key = input("k:\n")
cipher = encrypt(text, key)
print("\nencrypted：")
print(cipher)
plain = decrypt(text, key)
print("\ndecrypted：")
print(plain)