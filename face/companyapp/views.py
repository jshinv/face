# from django.shortcuts import render
# from django.http import HttpResponse
# # from companyapp.models import *

# # Create your views here.

# def index(request):
#     return render(
#         request, 'companyapp/index.html',
# )

from django.shortcuts import render
from django.http import HttpResponse
import socket

# from companyapp.models import *

# Create your views here.

def index(request):
    # person_data=Person.objects.all()
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.listen(0)
    client_socket,addr = server_socket.accept()
    data = client_socket.recv(65535)

    print(data.decode())

    return render(
        request,
            'companyapp/index.html',
            {   'data': data.decode()}
    )