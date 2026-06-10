import cv2

def rescale_frame(frame,scale=0.50):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[1]*scale)
    dimensions=(width, height)
    return cv2.resize(frame, dimensions)

capture=cv2.VideoCapture("C:\\Users\\ryani_jvpdg6k\\Videos\\dog.mp4")

while True:
    isTrue,frame=capture.read()
    frame_resized=rescale_frame(frame,scale=0.20)
    cv2.imshow("Original Video", frame)
    cv2.imshow("Resized Video", frame_resized)
    if cv2.waitKey(45) & 0XFF==ord("q"):
        break

capture.release()
cv2.destroyAllWindows()