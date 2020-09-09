import os
import cv2
import numpy as np
import glob
 
IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
    '.tif', '.TIF', '.tiff', '.TIFF']
def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)
def make_dataset(dir, max_dataset_size=float("inf")):
    images = []
    assert os.path.isdir(dir), '%s is not a valid directory' % dir

    for root, _, fnames in sorted(os.walk(dir)):
        for fname in fnames:
            if is_image_file(fname):
                path = os.path.join(root, fname)
                images.append(path)
    return images[:min(max_dataset_size, len(images))]

img_array = []
path = '' # which need to specify
image_paths = sorted(make_dataset(path))
print(image_paths)

for fname in image_paths:
	print(fname)
	print("-----------")
	img = cv2.imread(fname)
	height, width, layers = img.shape
    # print(height)
    # print(width)
    # print(layers)
	size = (width,height)
	img_array.append(img)
out = cv2.VideoWriter('synthetic_video.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
