# COMPUTING_HISTOGRAM.PY

img = cv.imread("gordy.jpg")
cv.imshow("Gordy", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
