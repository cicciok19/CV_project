import urllib.request
import cv2
import numpy as np
import os


def store_raw_images():
    #inserisci url delle immagini che vuoi salvare
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04037443'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    print(neg_image_urls)
    pic_num = 1

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
            img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

def resizeImage():
    img = cv2.imread("hand.jpg", cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(img, (100,100))
    cv2.imwrite("hand_good.jpg", resized_image)

if __name__ == '__main__':
   resizeImage()