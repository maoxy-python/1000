from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    return HttpResponse()


def demo(request):

    print("1111")
    print("3333")
    print("2222")

    return HttpResponse()

