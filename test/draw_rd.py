import os

import numpy as np
import cv2
import matplotlib.pyplot as plt

line = True

lstm_ssim = np.genfromtxt('test/lstm_ssim.csv', delimiter=',')
lstm_ssim = lstm_ssim[:-1]
if line:
    #lstm_ssim = np.mean(lstm_ssim, axis=0)
    lstm_bpp = np.arange(1, 17) / 192 * 24
    print(lstm_bpp.shape, lstm_ssim.shape)
    plt.plot(lstm_bpp, lstm_ssim, label='LSTM', marker='o')
else:
    lstm_bpp = np.stack([np.arange(1, 17) for _ in range(24)]) / 192 * 24
    plt.scatter(
        lstm_bpp.reshape(-1), lstm_ssim.reshape(-1), label='LSTM', marker='o')

jpeg_ssim = np.genfromtxt('test/jpeg_ssim.csv', delimiter=',')
jpeg_ssim = jpeg_ssim[:-1]
if line:
    pass
    #jpeg_ssim = np.mean(jpeg_ssim, axis=0)

jpeg_bpp = np.array([
    os.path.getsize('test/jpeg/{:02d}/{:02d}.jpg'.format(i, q)) * 8 /
    (cv2.imread('test/jpeg/{:02d}/{:02d}.jpg'.format(i, q))[:,:,::-1].size // 3)
    for i in range(0, 1) for q in range(1, 21)
])


if line:
    #jpeg_bpp = np.mean(jpeg_bpp, axis=0)
    print(jpeg_bpp.shape, jpeg_ssim.shape)
    plt.plot(jpeg_bpp, jpeg_ssim, label='JPEG', marker='x')
else:
    plt.scatter(
        jpeg_bpp.reshape(-1), jpeg_ssim.reshape(-1), label='JPEG', marker='x')

plt.xlim(0., 2.)
plt.ylim(0.7, 1.0)
plt.xlabel('bit per pixel')
plt.ylabel('MS-SSIM')
plt.legend()
plt.show()
plt.savefig('mssim.png')
