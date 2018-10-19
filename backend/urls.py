"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from app.views import CustomerList, CustomerDetail
from app.views import ProductList, ProductDetail
from app.views import AcountBalanceDetail
from app.views import InvoiceList, InvoiceDetail
from app.views import OrderList, OrderDetail
from rest_auth.registration.views import VerifyEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    path('api/customer/', CustomerList.as_view()),
    path('api/customer/<user_id>/', CustomerDetail.as_view()),
    path('api/product/', ProductList.as_view()),
    path('api/product/<product_id>/', ProductDetail.as_view()),
    path('api/balance/<user_id>/', AcountBalanceDetail.as_view()),
    path('api/invoice/<user_id>/', InvoiceList.as_view()),
    path('api/invoice/<user_id>/<invoice_number>/', InvoiceDetail.as_view()),
    path('api/order/<user_id>/', OrderList.as_view()),
    path('api/order/<user_id>/<order_id>/', OrderDetail.as_view()),
]
