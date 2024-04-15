import cv2
import numpy as np

#이미지 불러오기
img=cv2.imread("guitar.jpg")

#3-1) 1/25 평균필터 생성
kernel1 = np.ones((5,5))/25

# cv2.boxFilter() 함수를 사용하여 이미지 블러링 수행하기
blurred_img1 = cv2.boxFilter(img, -1, (5,5), kernel1)

#3-2) 수평 에지
kernel2 = np.array([[-1, -2, -3, -2, -1],
                    [-2, -4, -6, -4,- 2],
                    [0, 0, 0, 0, 0],
                    [2, 4, 6, 4, 2],
                    [1, 2, 3, 2, 1]])
# cv2.filter2D() 함수를 사용하여 이미지 블러링 수행하기
blurred_img2 = cv2.filter2D(img, -1, (5, 5), kernel2)

#3-3) cv2.GaussianBlur() 함수를 사용하여 이미지 블러링 수행하기
blurred_img3_sigma1 = cv2.GaussianBlur(img, (5, 5), sigmaX=1.0)
blurred_img3_sigma3 = cv2.GaussianBlur(img, (5, 5), sigmaX=3.0)
blurred_img3_sigma5 = cv2.GaussianBlur(img, (5, 5), sigmaX=5.0)


# 결과 이미지 출력하기
cv2.imshow("Blurred Image (cv2.boxFilter)", blurred_img1)
cv2.imshow("Blurred Image (cv2.filter2D)", blurred_img2)
cv2.imshow("Blurred Image Sigma 1 (cv2.GaussianBlur)", blurred_img3_sigma1)
cv2.imshow("Blurred Image Sigma 3 (cv2.GaussianBlur)", blurred_img3_sigma3)
cv2.imshow("Blurred Image Sigma 5 (cv2.GaussianBlur)", blurred_img3_sigma5)
cv2.waitKey(0)
cv2.destroyAllWindows()
