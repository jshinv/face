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
        if form.is_valid():
            logger.debug("2")
            recv_data = form.save(commit = False)
            logger.debug(recv_data)
            return render(request, 'companyapp/index.html',)
    else:
        #form = PostForm()
        return render(request, 'companyapp/index.html',)