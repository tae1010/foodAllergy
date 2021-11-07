from django.shortcuts import render, redirect
from .models import Allergy


# Create your views here.


def index(request):
    Allergy_list = Allergy.objects.order_by()
    context = {'Allergy_list': Allergy_list}
    return render(request, "foodAllergy/Allergy_list.html", context)


def detail(request):
    return render(request, 'foodAllergy/Allergy_detail.html')


def allergy_register(request):
    Allergy_list = Allergy.objects.order_by()
    context = {'Allergy_list': Allergy_list}
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
    Allergy_list = Allergy.objects.order_by()
    a = Allergy.objects.get(allergyName=allergy_name)
    context = {'allergyName': a, 'Allergy_list': Allergy_list}

    return render(request, 'foodAllergy/Allergy_register.html', context)


def addMyAllergy(request):
    check = request.POST.getlist('checkAllergy[]')
    Allergy_list = Allergy.objects.order_by()
    context = {'check': check, 'Allergy_list': Allergy_list}

    for allergy in Allergy_list:
        for ck in check:
            if ck == allergy.allergyName:
                allergy.myAllergy = "Y"
                allergy.save()

                for highAllergy in Allergy_list:
                    if highAllergy.allergyName == allergy.highLevelAllergy:
                        highAllergy.myAllergy = "Y"
                        highAllergy.save()

    return render(request, 'foodAllergy/Allergy_register.html', context)
