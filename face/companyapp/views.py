from django.shortcuts import render
from django.http import HttpResponse
# from companyapp.models import *

# Create your views here.

def index(request):
    return render(
        request, 'companyapp/index.html',
)

