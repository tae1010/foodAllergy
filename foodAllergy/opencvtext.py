from django.shortcuts import render
import cv2
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import numpy as np

def chImage(request):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    # 이미지 불러오기, Gray 프로세싱
    # 이미지 전처리
    image = cv2.imread("C:/Redbook/ch99/static/images/test07.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # gray = cv2.medianBlur(gray, ksize = 1)

    def opening(image):
        kernel = np.ones((1, 1), np.uint8)
        result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        return result
    gray = opening(gray)


    # 글자 프로세싱을 위해 Gray 이미지 임시파일 형태로 저장.
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)

    # Simple image to string
    text = pytesseract.image_to_string(Image.open(filename), lang='kor')
    arr = text.split('\n')[0:-1]
    text = '\n'.join(arr)
    os.remove(filename)

    text = {'text':text}
    return render(request, 'polls/Image_to_text.html', text)
