

# ------ Python Project 5 : Face Recognition Attendace System -----------



# Import all required modules

import face_recognition
import cv2
import numpy as np
from datetime import datetime
import csv


# Turn on the webcam
# video_capture = cv2.VideoCapture(0)
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video_capture.isOpened():
    print("Error: Could not open webcam.")
    exit()



# Load Known Faces

rohit_image = face_recognition.load_image_file("05_FacialReocgAttendanceSystem/Faces/Rohit_image.JPG")
rohit_encoding = face_recognition.face_encodings(rohit_image)[0]

om_image = face_recognition.load_image_file("05_FacialReocgAttendanceSystem/Faces/Om_image.png")
om_encoding = face_recognition.face_encodings(om_image)[0]

vaibhav_image = face_recognition.load_image_file("05_FacialReocgAttendanceSystem/Faces/Vaibhav_image.png")
vaibhav_encoding = face_recognition.face_encodings(vaibhav_image)[0]

ajinkya_image = face_recognition.load_image_file("05_FacialReocgAttendanceSystem/Faces/Ajinkya_image.jpg")
ajinkya_encoding = face_recognition.face_encodings(ajinkya_image)[0]


known_face_encodings = [rohit_encoding, om_encoding, vaibhav_encoding, ajinkya_encoding]

known_face_names = ["Rohit", "Om", "Vaibhav", "Ajinkya Darekar"]


# List of expected students
students = known_face_names.copy()



face_locations = []
face_encodings = []


# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)


while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Recognize Faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)

        # calculate best match index
        best_match_index = np.argmin(face_distance)
        name = "Unknown"

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]
        
        # Add the text if person is present
        if name in known_face_names:
            font=cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255,0,0)
            thickness = 3
            lineType = 2
            cv2.putText(frame,name+" Present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

        if name in students:
            students.remove(name)
            current_time = now.strftime("%H-%M%S") 
            lnwriter.writerow([name,current_time] )   

    cv2.imshow("Attendance", frame)
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break 


video_capture.release()
cv2.destroyAllWindows()
f.close()







