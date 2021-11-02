from django.shortcuts import render
from .models import Result
from .models import Allergy

# Create your views here.

def index(request):
    Result_list = Result.objects.order_by('-create_date')
    context = {'Result_list': Result_list}
    return render(request, "foodAllergy/Result_list.html",context)

def detail(request, Result_id):
    result = Result.objects.get(id=Result_id)
    context = {'Result': result}
    return render(request, 'foodAllergy/Result_detail.html', context)