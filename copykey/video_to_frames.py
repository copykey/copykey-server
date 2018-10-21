import cv2

#warning: this can only be called once per vid.
def video_to_frames(vid):
	if vid.isOpened() == False:
		return False
	frames = []
	while vid.isOpened():
		ret, frame = vid.read()
		if ret == True:
			frames.append(frame)
		else:
			break
	vid.release()
	return frames

#loads in a video from a path
def path_to_video(path):
	return cv2.VideoCapture(path)
