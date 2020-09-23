import cv2
import numpy as np
import matplotlib.pyplot as plt

def grab_frame(cap):
    """
    Method to grab a frame from the camera
    :param cap: the VideoCapture object
    :return: the captured image
    """
    ret, img = cap.read()
    return img

def bgr_to_rgb(image):
    """
    Convert a BGR image into RBG
    :param image: the BGR image
    :return: the same image but in RGB
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def main():
    #setting the camera
    print("Ciao")
    cap = cv2.VideoCapture(0)

    # enable Matplotlib interactive mode
    plt.ion()

    # create a figure to be updated
    fig = plt.figure()

    # prep a variable for the first run
    img = None

    #video to manage
    cap_video = cv2.VideoCapture("Prova.mp4")

    if(cap_video.isOpened() == False):
        print("Error in opening video")
    
    #setting the camera
    while (cap.isOpened() & cap_video.isOpened()):
    # get the current frame
        ret_video, frame_video = cap_video.read()
        frame = grab_frame(cap)
        if img is None:
            # convert it in RBG (for Matplotlib)
            img = plt.imshow(bgr_to_rgb(frame))
            plt.axis("off")  # hide axis, ticks, ...
            plt.title("Camera Capture")
            # show the plot!
            plt.show()
        else:
            # set the current frame as the data to show
            img.set_data(bgr_to_rgb(frame))
            # update the figure associated to the shown plot
            fig.canvas.draw()
            plt.pause(1/30)  # pause: 30 frames per second
        if ret_video == True:
            cv2.imshow('frame', frame_video)
        else:
            break

    #releasing video
    cap.release()
    cap_video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)