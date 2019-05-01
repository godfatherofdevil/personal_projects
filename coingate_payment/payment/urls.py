from django.urls import path
from payment import views

urlpatterns = [
    path('index/', views.order_status, name='order_status'),
    path('proceed/<int:payment_price>/', views.payment_proceed, name='payment_proceed'),
    path('callback/', views.callback, name='callback'),
    path('cancel/', views.cancel, name='cancel'),
    path('success/', views.success, name='success'),
]
