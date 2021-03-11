# READING IMAGES
img = cv.imread("gordy.jpg")
# Reads the image
cv.imshow("Gordy", img)
# Displays the image
cv.waitKey(0)
# Keyboard binding function

# READING VIDEOS
def rescaleFrame(frame, scale=0.75):
    # Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, )
    Resize image or video

# Works for live video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture(0, cv.CAP_DSHOW)
# Reads video
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)
    # Captures every frame of the video

    # Press "q" to exit
    if cv.waitKey(20) & 0xff == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
# Destroys the window
