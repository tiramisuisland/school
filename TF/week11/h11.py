import cv2
import matplotlib.pyplot as plt

# 讀取影像
img = cv2.imread('TF\week11\Ruihang_Ai.jpg', cv2.IMREAD_GRAYSCALE)

# 不同的二值化方法
methods = [
    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV
]
method_names = [
    'THRESH_BINARY',
    'THRESH_BINARY_INV',
    'THRESH_TRUNC',
    'THRESH_TOZERO',
    'THRESH_TOZERO_INV'
]

plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

for i, method in enumerate(methods):
    _, thresh = cv2.threshold(img, 127, 255, method)
    plt.subplot(2, 3, i + 2)
    plt.title(method_names[i])
    plt.imshow(thresh, cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()