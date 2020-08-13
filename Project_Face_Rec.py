import os
from cv2 import cv2
import face_recognition


KNOWN_FACES_DIR = "Project_Face_Rec/known_faces"
UNKNOWN_FACES_DIR = "Project_Face_Rec/unknown_faces"
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

print("loading known faces")

known_faces = []
known_names = []

# learn
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

# use
print("process unknown faces")
for filename in os.listdir(UNKNOWN_FACES_DIR):
    print(filename)
    image = face_recognition.load_image_file(f'{UNKNOWN_FACES_DIR}/{filename}')
    locations = face_recognition.face_locations(image, model = MODEL)
    encodings = face_recognition.face_encodings(image, locations)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_encoding, face_location in zip(encodings, locations):
        result = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        match = None
        if True in result:
            match = known_names[result.index(True)]
            print(f"Match found: {match}")

            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1], face_location[2])
            color = [0, 255, 0]
            cv2.rectangle(image, top_left, bottom_right, color, FRAME_THICKNESS)
            
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1], face_location[2]+22)
            cv2.rectangle(image, top_left, bottom_right, color, cv2.FILLED)
            cv2.putText(image, match, (face_location[3]+10, face_location[2]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)

    cv2.imshow(filename, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


