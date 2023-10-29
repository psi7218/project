from django.urls import path
from . import views

urlpatterns = [
    path('save_deposit_products/', views.save_deposit_products),
    path('deposit_products/', views.deposit_products ),
    path('deposit_product_options/<str:fin_prdt_cd>/', views.deposit_product_options),
    path('deposit_products/top_rate/', views.top_rate)
]