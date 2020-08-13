from cv2 import cv2
import os

path = r'Project_Face_Rec/known_faces'

while True:
    print('1. Add User''s Face\n2. Exit')
    print('Your choice: ')
    choice = int(input())


    if choice == 1:
        print('Enter your name: ')
        user_name = input()
        if len(user_name) == 0:
            break
        else:
            # create directory
            try:
                os.mkdir(f'{path}/{user_name}/')
            except OSError:
                print ("Creation of the directory %s failed" % path)
            else:
                path = f'{path}/{user_name}/'
                print ("Successfully created the directory %s " % path)
                
                cam = cv2.VideoCapture(0)

                cv2.namedWindow("test")

                img_counter = 0
                
                while True:
                    ret, frame = cam.read()
                    cv2.imshow("test", frame)
                    if not ret:
                        break
                    k = cv2.waitKey(1)

                    if k%256 == 27:
                        # ESC pressed
                        print("Escape hit, closing...")
                        break
                    elif k%256 == 32:
                        # SPACE pressed
                        img_name = "opencv_frame_{}.png".format(img_counter)
                        if not os.path.isdir(path):
                            print("No such a directory: {}".format(path))
                            exit(1)
                        cv2.imwrite(os.path.join(path, img_name), frame)
                        print("{} written!".format(img_name))
                        img_counter += 1

                cam.release()
                cv2.destroyAllWindows()
    elif choice == 2:
        break

