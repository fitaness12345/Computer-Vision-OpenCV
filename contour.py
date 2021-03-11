 # CONTOURS.PY


# Contour Detection
img = cv.imread("gordy.jpg")
cv.imshow("Gordy", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

ret, thresh = cv.threshold(gray, 105, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)}contour(s)")
# Shows how many contours in the canny image

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow("Contours Drawn", blank)
# Draw contours on blank image

# Contour video
cap = cv.VideoCapture(0,cv.CAP_DSHOW)
while True:
    ret, img = cap.read()

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    canny = cv.Canny(blur, 10, 70)
    ret, mask = cv.threshold(canny, 70, 255, cv.THRESH_BINARY)
    cv.imshow('Video feed', mask)

    if cv.waitKey(20) & 0xff == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
