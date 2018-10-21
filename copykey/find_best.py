import cv2
import numpy as np

def find_best(num_desired, images):
	laplacian_variances = []
	for image in images:
		height, width, _ = image.shape
		canny = cv2.Canny(image, 60, 135)
		laplacian_variances.append([image, cv2.Laplacian(canny, cv2.CV_64F).var() * width])
	laplacian_variances.sort(key=lambda x: -x[1])
	return [i[0] for i in laplacian_variances[0:num_desired]]
