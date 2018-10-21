import cv2
from copykey import find_best
from copykey import video_to_frames
from copykey import find_rectangle
from shutil import copyfile
import os

def run(input, output, error):
	video = video_to_frames.path_to_video(input)
	frames = video_to_frames.video_to_frames(video)

	if frames == False:
		copyfile(error, output)

	key_images = []
	for frame in frames:
		success, key_image, _ = find_rectangle.process(frame)
		if success:
			key_images.append(key_image)
	results = find_best.find_best(1, key_images)
	cv2.imwrite(output, results[0])
	os.remove(input)
