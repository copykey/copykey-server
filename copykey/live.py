import cv2
from copykey import find_rectangle

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()
	if ret == False:
		break
	success, key, drawn = find_rectangle.process(frame)
	if success:
		cv2.imshow("key", key)
	cv2.imshow("drawn", drawn)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

