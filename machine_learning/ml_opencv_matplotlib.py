# ml_opencv_matplotlib.py
import pandas as pd
import numpy as np
import cv2
from glob import glob
import matplotlib.pylab as plt

#reading data inside pngs
ram_dog_files = glob("/home/caratred/AUTOCAD/*.jpg")
# print(ram_dog_files,"////////////")

#reading data inside jpg using matplotlib (plt)
plt_reading_image = plt.imread(ram_dog_files[0])
# print("array_format_of_image : -------------------",plt_reading_image)
print("shape of image",plt_reading_image.shape)

image_flatten = plt_reading_image.flatten()
# print(image_flatten,"?????????????????",plt_reading_image.max())
scatter_graph_of_image = pd.Series(image_flatten).plot(kind="hist",bins=50,title="uiui")
plt_reading_image.show()


# also importing images using cv2
cv2_reading_image = cv2.imread(ram_dog_files[0])
# print("array_format_of_image : -------------------",cv2_reading_image)
print("shape of image",cv2_reading_image.shape)