from django.http import JsonResponse
from django.shortcuts import render


def salom(request):
    return  JsonResponse({'massage':'Hello DRF'})
