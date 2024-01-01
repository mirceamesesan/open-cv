import cv2
import numpy as np

video_url = "./assets/videos/AdobeStock_203290125_Video_HD_Preview.mov"

cap = cv2.VideoCapture(0)
# cap = cv.VideoCapture(video_url)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    half_image = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # top left
    image[:height//2, :width//2] = cv2.rotate(half_image, cv2.ROTATE_180)
    # top right
    image[:height//2, width//2:] = half_image
    # bottom left
    image[height//2:, :width//2] = half_image
    # bottom right
    image[height//2:, width//2:] = cv2.rotate(half_image, cv2.ROTATE_180)

    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
