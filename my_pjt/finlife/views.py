from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DepositProducts, DepositOptions
from django.conf import settings

API_KEY = settings.API_KEY
# Create your views here.
# api_key = settings.API_KEY
# 568c302d4a9167e7248f17f6e13d6968
@api_view(["GET"])
def save_deposit_products(request):
    pass

@api_view(["GET", "POST"])
def deposit_products(request):
    pass

@api_view(["GET"])
def deposit_product_options(request,fin_prdt_cd):
    pass

@api_view(["GET"])
def top_rate(request):
    pass