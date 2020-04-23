from django.shortcuts import render, redirect
from django.http import HttpResponse
# from companyapp.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger('default')
user_ip_list = []

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    logger.debug("----- enter index -----")
    return render(
        request, 'companyapp/index.html',
)

def post1(request):
    if request.method == "POST":
        user_ip = get_client_ip(request)
        if user_ip in user_ip_list:
            pass
        else:
            user_ip_list.append(user_ip)
        logger.debug("----- CAM {} -----".format(user_ip_list.index(user_ip)))
        form = Person(request.POST)
        logger.debug(form)

        userName = request.POST.getlist('userName')[0]
        checkDay = request.POST.getlist('checkDay')[0]
        inTime = request.POST.getlist('inTime')[0]
        outTime = request.POST.getlist('outTime')[0]

        #if Person.objects.filter(username=userName, checkday=checkDay).exists() == False:
        
        if user_ip_list.index(user_ip) == 0:
            # 1. Ãâ±Ù - CAM 0
            Person(
                username=userName,
                checkday=checkDay,
                intime=inTime).save()
        elif user_ip_list.index(user_ip) == 1:
            # 2. Åð±Ù - CAM 1
            #if Person.objects.filter(username=userName, checkday=checkDay).exists() == False:
            temp_id = Person.objects.filter(username=userName, checkday=checkDay).values_list('id', flat=True)
            #logger.debug(temp_id[0])
            temp = Person.objects.get(id=temp_id[0])
            #logger.debug(temp)
            temp.outtime = outTime
            temp.save()
    else:
        #form = PostForm()
        return render(request, 'companyapp/index.html',)