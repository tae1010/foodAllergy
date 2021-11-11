from django.shortcuts import render, redirect
from .models import Allergy, Result
import datetime
import cv2
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import numpy as np

# Create your views here.

def index(request):
    allergy_list = Allergy.objects.order_by()
    context = {'allergy_list': allergy_list}
    return render(request, "foodAllergy/main.html", context)


def detail(request):
    return render(request, 'foodAllergy/result_load.html')


def allergy_register(request):
    allergy_list = Allergy.objects.order_by()
    context = {'allergy_list': allergy_list}
    return render(request, 'foodAllergy/Allergy_register.html', context)


def regist(request):
    allergy_list = Allergy.objects.order_by()
    allergy_names = []
    allergy_Lv2 = []

    highLevelAllergy = request.POST.get('highLevelAllergy')
    allergyLv1 = request.POST.get('allergyName')

    for allergy in allergy_list:
        if allergy.level == 2 and allergy.highLevelAllergy == allergyLv1:
            allergy_Lv2.append(allergy.allergyName)


    for allergy in allergy_list:
        allergy_names.append(allergy.allergyName)

    # 둘다 비어있을때
    if allergyLv1 == "" and highLevelAllergy == "":
        print("입력해주세요")

    #
    elif allergyLv1 == "":
        print("lv1만 적던가 둘다 적어주세요")

    else:
        # 첫번째 칸만 써있고 첫번째 칸이 중복이 아닐때
        if highLevelAllergy == "" and allergyLv1 not in allergy_names:
            level = 1
            a = Allergy(allergyName=allergyLv1, highLevelAllergy=highLevelAllergy,
                        level=level, myAllergy="N")
            a.save()

        # 첫번째칸만 써있고 중복일때
        elif highLevelAllergy == "" and allergyLv1 in allergy_names:
            print("Lv1 중복입니다!!!!!!!!!!")

        # 둘다 써있을때
        else:
            # 둘다 써있는데 LV1,LV2 모두겹치면 오류메시지
            if allergyLv1 in allergy_names and highLevelAllergy in allergy_Lv2:
                print("lv1, lv2 둘다 중복입니다")

            # 둘다 써있는데 lv1이 없으면 lv1도 추가
            elif allergyLv1 not in allergy_names:
                a = Allergy(allergyName=allergyLv1, highLevelAllergy="",
                            level=1, myAllergy="N")
                a.save()

                a = Allergy(allergyName=highLevelAllergy, highLevelAllergy=allergyLv1,
                            level=2, myAllergy="N")
                a.save()
            else:
                a = Allergy(allergyName=highLevelAllergy, highLevelAllergy=allergyLv1,
                            level=2, myAllergy="N")
                a.save()

    return redirect('foodAllergy:register')


def showLv2(request, allergy_name):
    allergy_list = Allergy.objects.order_by()
    allergy_high = []

    global find_high  # 알러지 추가할때 레벨2 체크하기전 레벨1이 뭔지 저장
    find_high = allergy_name

    count = 0

    for allergy in allergy_list:
        allergy_high.append(allergy.highLevelAllergy)

    if allergy_name not in allergy_high:
        count = 1

    print(allergy_high)

    a = Allergy.objects.get(allergyName=allergy_name)
    context = {'allergyName': a, 'allergy_list': allergy_list, 'count': count}

    return render(request, 'foodAllergy/Allergy_register.html',context)


def myshowLv2(request, allergy_name):
    allergy_list2 = Allergy.objects.order_by()

    global find_high  # 알러지 추가할때 레벨2 체크하기전 레벨1이 뭔지 저장
    find_high = allergy_name

    count2 = 0

    for allergy in allergy_list2:
        count2 = 1
        if allergy_name == allergy.highLevelAllergy and allergy.myAllergy == "Y":
            count2 = 0
            break

    a2 = Allergy.objects.get(allergyName=allergy_name)
    context = {'allergyName2': a2, 'allergy_list2': allergy_list2, 'count2': count2}

    return render(request, 'foodAllergy/Allergy_register.html',context)


def addMyAllergy(request):
    check = request.POST.getlist('checkAllergy[]')
    allergy_list = Allergy.objects.order_by()
    context = {'check':check, 'allergy_list': allergy_list}
    # current_url = resolve(request.path_info).url_name
    allergy_high = []

    print(check)
    global find_high
    print("find_high : " + find_high)

    for allergy in allergy_list:
        allergy_high.append(allergy.highLevelAllergy)

    for allergy in allergy_list:
        for ck in check:
            if ck == allergy.allergyName:
                if allergy.highLevelAllergy == find_high:
                    allergy.myAllergy = "Y"
                    allergy.save()

                    for highAllergy in allergy_list:
                        if highAllergy.allergyName == allergy.highLevelAllergy:
                            highAllergy.myAllergy = "Y"
                            highAllergy.save()

                elif find_high not in allergy_high:
                    allergy.myAllergy = "Y"
                    allergy.save()

    return render(request, 'foodAllergy/Allergy_register.html', context)


def deleteMyAllergy(request):
    check = request.POST.getlist('checkAllergy2[]')
    allergy_list = Allergy.objects.order_by()
    allergy_my = []

    global find_high
    print("find_high : " + find_high)

    for allergy in allergy_list:
        for ck in check:
            if ck == allergy.allergyName:
                if allergy.highLevelAllergy == find_high:
                    allergy.myAllergy = "N"
                    allergy.save()

    allergy_list = Allergy.objects.order_by()

    for allergy in allergy_list:
        if allergy.highLevelAllergy == find_high:
            allergy_my.append(allergy.myAllergy)

    print(allergy_my)

    if 'Y' not in allergy_my:
        for allergy in allergy_list:
            if allergy.allergyName == find_high:
                allergy.myAllergy = "N"
                allergy.save()

    context = {'check2': check, 'allergy_list2': allergy_list}

    return render(request, 'foodAllergy/Allergy_register.html', context)


# ------------------------------------------------------------------------------


def resultLoad(request):
    result_list = Result.objects.order_by()
    context = {'result_list': result_list}
    return render(request, 'foodAllergy/result_load.html', context)


def detailResult(request, result_name):
    result_list = Result.objects.order_by()
    result = Result.objects.get(productName=result_name)
    context = {'result_list': result_list, 'result': result}
    return render(request, 'foodAllergy/result_load.html', context)


def resultSave(request):
    f_productName = request.POST.get('f_productName')
    f_productContent = request.POST.get('f_productContent')
    f_exist = request.POST.get('f_exist')
    now = datetime.datetime.now()
    f_exist = f_exist.strip().replace("\n", "").replace(" ","")

    a = Result(productName=f_productName, productContent=f_productContent,
                allergyResult=f_exist, create_date=now)
    a.save()

    return redirect('foodAllergy:index')

#-------------------------------------------------------------

def chImage(request):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    # 이미지 불러오기, Gray 프로세싱
    # 이미지 전처리
    image = cv2.imread("C:/Users/kjt/PycharmProjects/pythonProject/static/images/test05.jpg")
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
    text = text.strip().replace("\n", "")

    allergy_list = Allergy.objects.order_by()
    exist_allergy = []

    for allergy in allergy_list:
        if allergy.myAllergy == "Y":
            if text.find(allergy.allergyName) != -1:
                exist_allergy.append(allergy.allergyName)

    text = {'text':text, 'exist_allergy':exist_allergy}
    return render(request, 'foodAllergy/main.html', text)
