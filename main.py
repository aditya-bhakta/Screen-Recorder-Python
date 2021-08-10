import datetime
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
time = datetime.datetime.now().strftime('%d %H-%M-%S')
file_name = f'Time{time}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (w, h))

while True:
    img = ImageGrab.grab(bbox=(0, 0, w, h))
    img_np = np.array(img)
    final_image = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Your Screen', final_image)

    captured_video.write(final_image)
    if cv2.waitKey(10) == ord("q"):
        break
