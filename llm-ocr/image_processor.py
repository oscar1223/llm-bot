###
# Class that processes images using an OCR
###


import cv2
import numpy as np
import pytesseract
import var_c

pytesseract.pytesseract.tesseract_cmd = var_c.path_tesseract
custom_config = var_c.custom_config



# Binarization method
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Noise reduction method
def noise_removal(imagen):
    kernel = np.ones((1, 1), np.uint8)
    imagen = cv2.dilate(imagen, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    imagen = cv2.erode(imagen, kernel, iterations=1)
    imagen = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)
    imagen = cv2.medianBlur(imagen, 3)
    return imagen

# Erosion method
def thin_font(imagen):
    imagen = cv2.bitwise_not(imagen)
    kernel = np.ones((2, 2), np.uint8)
    imagen = cv2.erode(imagen, kernel, iterations=1)
    imagen = cv2.bitwise_not(imagen)

    return imagen

# Dilation method
def thick_font(imagen):
    imagen = cv2.bitwise_not(imagen)
    kernel = np.ones((2, 2), np.uint8)
    imagen = cv2.dilate(imagen, kernel, iterations=1)
    imagen = cv2.bitwise_not(imagen)

    return imagen

# Rotation method
def getSkewAngle(cvImage) -> float:

    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)


    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x, y, w, h = rect
        cv2.rectangle(newImage, (x, y), (x + w, y + h), (0, 255, 0), 2)


    largestContour = contours[0]
    print(len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("temp/boxes.jpg", newImage)


    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle

def rotate_imagen(cvImagen, angle: float):
    newImage = cvImagen.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage

def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotate_imagen(cvImage, -1.0 * angle)

# Border cleaning method
def remove_borders(imagen):
    contours, heiarchy = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x: cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = imagen[y:y + h, x:x + w]
    return (crop)

# Rescaling image
def rescaling_image(image):
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    return image


# Processing method
def preprocess_finale(imagen, im_path):
    resize_image = rescaling_image(imagen)
    cv2.imwrite(im_path, resize_image)

    gray_imagen = grayscale(imagen)
    cv2.imwrite(im_path, gray_imagen)
    thresh, im_bw = cv2.threshold(gray_imagen, 210, 230, cv2.THRESH_BINARY)
    cv2.imwrite(im_path, im_bw)

    no_noise = noise_removal(im_bw)

    cv2.imwrite(im_path, no_noise)

    eroded_imagen = thin_font(no_noise)
    cv2.imwrite(im_path, eroded_imagen)


    dilated_imagen = thick_font(no_noise)
    cv2.imwrite(im_path, dilated_imagen)


    new = cv2.imread(im_path)
    fixed = deskew(new)
    cv2.imwrite(im_path, fixed)


    no_borders = remove_borders(no_noise)
    cv2.imwrite(im_path, no_borders)
    color = [255, 255, 255]
    top, bottom, left, right = [150] * 4

    image_with_border = cv2.copyMakeBorder(no_borders, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    cv2.imwrite(im_path, image_with_border)

    return imagen


