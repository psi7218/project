from django.urls import path
from . import views

urlpatterns = [
    path('finlife/save_deposit_products/', views.save_deposit_products, name="save_deposit_products"),
    path('finlife/deposit_products/', views.deposit_products, name="deposit-products"),
    path('finlife/deposit_product_options/<str:fin_prdt_cd>/', views.deposit_product_options, name="deposit_product_options"),
    path('finlife/deposit_priducts/top_rate/', views.top_rate, name="top_rate")
]