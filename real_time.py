from cv2 import cv2
from random import randrange
import face_recognition
import os
import pickle
import time

KNOWN_FACES_DIR = "Project_Face_Rec/known_faces"
UNKNOWN_FACES_DIR = "Project_Face_Rec/unknown_faces"
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

print("loading known faces")

known_faces = []
known_names = []

#### #### #### #### #### #### #### #### ####                         learn                          #### #### #### #### #### #### #### #### #### 
for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
        image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}/{filename}')
        
        # This has nothing to do with this library. This is a bug in your own code. 
        # The face_recognition.face_encodings(unknown_image) function returns an array with one element for each face detected in the image. 
        # If you check the first element of the array directly (i.e. element [0]) without first testing the length of the array, 
        # you'll get this error if no faces were detected in the image.
        encoding = face_recognition.face_encodings(image)
        if (len(encoding) > 0):
            encoding = encoding[0]
            known_faces.append(encoding)
            known_names.append(name)
        # another way
        #encoding = pickle.load(open(f"{KNOWN_FACES_DIR}/{name}/{filename}", "rb"))
        #known_faces.append(encoding)
        #known_names.append(name)

if len(known_names) > 0:
    next_id = len(known_names) + 1
else:
    next_id = 0

#### #### #### #### #### #### #### #### ####                         recogize                          #### #### #### #### #### #### #### #### #### 

# load some pre-train data on face frontals from openCV (haar cascade algorithm)
#trained_face_data = cv2.CascadeClassifier('Project_Face_Rec/haarcascade_frontalface_default.xml')
print("start")
# capture video from webcam
webcam = cv2.VideoCapture(0)
### iterate foverever over frames
while True:
    # read the current frame
    successful_frame_read, frame = webcam.read()

    locations = face_recognition.face_locations(frame, model = MODEL)
    encodings = face_recognition.face_encodings(frame, locations)

    for face_encoding, face_location in zip(encodings, locations):
        results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in results:
            match = known_names[results.index(True)]
            print(f"Match found: {match}")
        else:
            match = str(next_id)
            next_id += 1
            known_names.append(match)
            known_faces.append(face_encoding)
            os.mkdir(f"{KNOWN_FACES_DIR}/{match}")
            pickle.dump(face_encoding, open(f"{KNOWN_FACES_DIR}/{match}/{match}-{int(time.time())}.pkl", "wb"))

        top_left = (face_location[3], face_location[0])
        bottom_right = (face_location[1], face_location[2])
        color = [0, 255, 0]
        cv2.rectangle(frame, top_left, bottom_right, color, FRAME_THICKNESS)    

        top_left = (face_location[3], face_location[2])
        bottom_right = (face_location[1], face_location[2] + 22)
        cv2.rectangle(frame, top_left, bottom_right, color, cv2.FILLED)
        cv2.putText(frame, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200))


    """ jusr detection
    # must to convert to grayscale
    # grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    #face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # draw rectangles & put name
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 10)

    # stop
    if cv2.waitkey(1) & 0xFF == ord("q")
        break """

    cv2.imshow('Clever Programmer Face Detector', frame)      
    key = cv2.waitKey(1)

    # stop if press esc
    if key%256 == 27:
        print("Escape hit, closing...")
        break

# release the video capture project
# webcam.release()

print("Code completed")


