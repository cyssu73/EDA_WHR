from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def eda(request):
    return render(request,'whr_eda.html',{})