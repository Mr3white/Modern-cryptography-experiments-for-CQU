import copy
import cv2
import numpy as np
import matplotlib.pyplot as plt

def arnold(img, key):
    N, a, b, c, d = key
    h, w = img.shape[: 2]
    new_img = copy.deepcopy(img)
    # 置换N次
    for i in range(N):
        for x in range(h):
            for y in range(w):
                nx = ((a * x + b * y) % w + w) % w
                ny = ((c * x + d * y) % w + w) % w
                nx = int(nx)
                ny = int(ny)
                new_img[nx, ny] = img[x, y]
        img = copy.deepcopy(new_img)
    return new_img

def iarnold(img, key):
    N, a, b, c, d = key
    # 求矩阵逆
    matrix = np.mat([[a, b], [c, d]]).I
    # 精度问题
    [[a, b], [c, d]] = matrix.tolist()
    return arnold(img, [N, a, b, c, d])

a = 1
b = 1
c = 1
d = 2
N = 50
img = cv2.imread('./lena_gray.bmp')
img_encrypted = arnold(img, [N, a, b, c, d])
plt.imshow(img_encrypted)
plt.show()
#cv2.imwrite('arnode_50.jpg',img_encrypted)
img_decrypted = iarnold(img_encrypted, [N, a, b, c, d])
plt.imshow(img_decrypted)
plt.show()