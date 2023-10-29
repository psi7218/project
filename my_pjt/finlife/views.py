from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DepositProducts, DepositOptions
from django.conf import settings
import requests
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
from django.http.response import JsonResponse

API_KEY = settings.API_KEY
# Create your views here.
# api_key = settings.API_KEY
# 568c302d4a9167e7248f17f6e13d6968
@api_view(["GET"])
def save_deposit_products(request):    
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    result = response.get('result')
    baseList = result.get('baseList')
    optionList = result.get('optionList')
    
    for li in baseList:
        save_data = {
            'fin_prdt_cd' : li["fin_prdt_cd"],
            'kor_co_nm' : li["kor_co_nm"],
            'fin_prdt_nm' : li["fin_prdt_nm"],
            'etc_note' : li['etc_note'],
            'join_deny' : li['join_deny'],
            'join_member' : li['join_member'],
            'join_way' : li['join_way'],
            'spcl_cnd' : li['spcl_cnd'],
        }
        
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    for option in optionList:
        
        option_data = {
            'fin_prdt_cd' : option.get('fin_prdt_cd'),
            'intr_rate_type_nm' : option.get('intr_rate_type_nm'),
            'intr_rate' : option.get('intr_rate'),
            'intr_rate2' : option.get('intr_rate2'),
            'save_trm' : option.get('save_trm'),
        }        
        product = get_object_or_404(DepositProducts, fin_prdt_cd=option.get('fin_prdt_cd'))
        serializer = DepositOptionsSerializer(data=option_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
            
            
            
            
    return Response({'message': 'ok'})
    
    

@api_view(["GET", "POST"])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
    #응답할 수 있는 형태(JSON)로 포장
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET"])
def deposit_product_options(request,fin_prdt_cd):
    option = get_list_or_404(DepositOptions, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(option, many=True)
    return Response(serializer.data)


def top_rate(request):
    top_rates = DepositOptions.objects.all()    
    result = max(top_rates, key=lambda x:x.intr_rate2) 
  
    max_product = DepositProducts.objects.get(fin_prdt_cd=result.fin_prdt_cd)
  
    serializer = DepositProductsSerializer(max_product)
    serializer_option = DepositOptionsSerializer(result)
    context = {
        'deposit_product' : serializer.data,
        'options' : [serializer_option.data]
    }
    
    return JsonResponse(context)
