from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('account/create', views.AccountCreateView.as_view(), name='account_create'),
]