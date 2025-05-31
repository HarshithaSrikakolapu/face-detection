import cv2

haar_cascade = cv2.CascadeClassifier(r"c:\Users\HP\Downloads\haarcascade_frontalface_default.xml")


cam = cv2.VideoCapture(0)  

if not cam.isOpened():
    print("Error: Cannot open webcam")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Face Detection", frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break


cam.release()
cv2.destroyAllWindows()
