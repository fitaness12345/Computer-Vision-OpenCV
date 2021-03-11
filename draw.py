#DRAW

blank = np.zeros((500,500,3),dtype="uint8")
cv.imshow("Blank", blank)
# Creates a blank page

# Paints the image
blank[200:300, 300:400] = 0,255,0
cv.imshow("Green", blank)

# Draw a rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow("Rectangle", blank)

# Draw a circle
cv.circle(blank,(250,250), 40,(0,0,255),thickness=2)
cv.imshow("Circle", blank)

# Draw a line
cv.line(blank, (0,0), (250,250),(255,0,0),thickness=3)
cv.imshow("Line", blank)

# Write text on an image
cv.putText(blank, "Hello World!", (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)
