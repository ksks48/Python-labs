import cv2

# Завантаження зображення
image = cv2.imread('image.jpg')

# Відображення зображення
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
