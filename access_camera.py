import cv2
import sys

# default camera index
s = 0
#check if there is command line specification to override that value
if len(sys.argv) > 1:
    s = sys.argv[1]

#call the video capture class and pass it the value of "s" i.e the index of camera i.e default camera 0
source = cv2.VideoCapture(s)

#creating a window for output
win_name = 'Camera Preview'
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
# continuously stream untill user hits esc key
while cv2.waitKey(1) != 27: # Escape checks if esc key is pressed
    has_frame, frame = source.read() # has frame checks for frame and source.read imports it
    if not has_frame: #if no frames from the sourcec i.e camera then the loop breaks
        break
    cv2.imshow(win_name, frame)

source.release() # cuts connection with the camera
cv2.destroyWindow(win_name) #destroys the window
