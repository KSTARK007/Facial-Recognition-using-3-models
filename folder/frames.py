import os
import cv2
pathOut = r"C:\\Users\\kiran\\OneDrive\\Desktop\\ML project\\folder\\extractedframes\\"
count = 0
frameno = 0
counter = 1
listing = os.listdir(r'./')
for vid in listing:
    vid = r"./"+vid
    cap = cv2.VideoCapture(vid)
    count = 0
    counter += 1
    success = True
    while success:
        success,image = cap.read()
        if count%30 == 0 :
            cv2.imwrite(pathOut + 'frame%d.jpg'%count,image)
            print(frameno)
            frameno+=1
        count+=1