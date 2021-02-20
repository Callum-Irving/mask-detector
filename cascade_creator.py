import os
import numpy as np
import cv2


def create_usable_images():
    if not os.path.exists("datasets/positive"):
        os.makedirs("datasets/positive")
    if not os.path.exists("datasets/negative"):
        os.makedirs("datasets/negative")

    image_index = 0
    for filename in os.listdir("datasets/pos"):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image = cv2.imread("datasets/pos/" + filename,
                               cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (100, 100))
            cv2.imwrite("datasets/positive/" +
                        str(image_index) + ".jpg", image)
            image_index += 1

    image_index = 0
    for filename in os.listdir("datasets/neg"):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image = cv2.imread("datasets/neg/" + filename,
                               cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (100, 100))
            cv2.imwrite("datasets/negative/" +
                        str(image_index) + ".jpg", image)
            image_index += 1


def create_positive_overlays():
    index = 0
    for filename in os.listdir("datasets/Mask images"):
        image = cv2.imread("datasets/Mask images/" + filename)
        image = cv2.resize(image, (50, 50))
        cv2.imwrite("datasets/Mask images/" + str(index) + ".jpg", image)
        index += 1


def create_descriptions():
    for image in os.listdir("datasets/negative"):
        desc = "negative/" + image + "\n"
        with open("bg.txt", "a") as f:
            f.write(desc)


create_positive_overlays()
