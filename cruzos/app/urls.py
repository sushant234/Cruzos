from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    # path('product', views.product, name='product'),
    url(r'^product/(?P<value>\d+)/$', views.products,name='product'),
    path('services', views.services, name='services'),
    # path('orderform', views.orderform, name='orderform'),
    url(r'^orderform/(?P<value>\d+)/$', views.orderform,name='orderform'),
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    path('T&C', views.tc, name='T&C'),
    path('extends', views.extends, name='extends'),
    path('payment_status', views.payment_status, name='payment_status'),
    path('cart_add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart_detail',views.cart_detail,name='cart_detail'),
    path('item_increment/<int:id>/',views.item_increment,name='item_increment'),
    path('item_decrement/<int:id>/',views.item_decrement,name='item_decrement'),
    path('item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('contactus', views.contactus, name='contactus'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)