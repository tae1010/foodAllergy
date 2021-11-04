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
    return render(request,'foodAllergy/Allergy_register.html', context)


def regist(request):

    highLevelAllergy = request.POST.get('highLevelAllergy')
    if highLevelAllergy == "":
        level = 1
        a = Allergy(allergyName=request.POST.get('allergyName'), highLevelAllergy=highLevelAllergy,
                    level=level, myAllergy="N")
    else:
        level = 2
        a = Allergy(allergyName=highLevelAllergy, highLevelAllergy=request.POST.get('allergyName'),
                    level=level, myAllergy="N")

    a.save()

    return redirect('foodAllergy:register')


def showLv2(request, allergy_name):
    Allergy_list = Allergy.objects.order_by()
    a = Allergy.objects.get(allergyName=allergy_name)
    context = {'allergyName' : a, 'Allergy_list': Allergy_list}

    return render(request, 'foodAllergy/Allergy_register.html',context)
