import cv2

data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv2.imread('img1.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = data.detectMultiScale(gray)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# cv2.imshow('img',img)
# cv2.waitKey()

cap = cv2.VideoCapture(0)
while(True):
    suframe, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = data.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('img',frame)
    key=cv2.waitKey(1)
    if(key==ord('Q') or key==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()

print("finished")