import cv2
img = cv2.imread("C:/Users/vindy/Downloads/PRO-c116-OpenCV-Image-Assets-main/butterfly.jpg")
cv2.imshow("display image",img)
print(img)
grey_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("Retro image",grey_img)

cv2.waitKey(0)