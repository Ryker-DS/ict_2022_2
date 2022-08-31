import os
import cv2

IMG_PATH = "../images"
SAVE_PATH = "../images"

if __name__ == "__main__":
    img = cv2.imread(os.path.join(IMG_PATH, "lena.jpeg"))

    lower_reso = cv2.pyrDown(img)
    higher_reso = cv2.pyrUp(img)
    lower_reso1 = cv2.pyrDown(lower_reso)
    higher_reso1 = cv2.pyrUp(higher_reso)

    cv2.imshow('img', img)
    cv2.imshow('lower', lower_reso)
    cv2.imshow('higher', higher_reso)
    cv2.imwrite(SAVE_PATH + 'lower_reso1.png', lower_reso1)
    cv2.imwrite(SAVE_PATH + 'higher_reso1.png', higher_reso1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()