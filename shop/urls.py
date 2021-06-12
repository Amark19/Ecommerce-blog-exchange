from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='Aboutus'),
    path('contact/',views.contact,name='Contactus'),
    path('tracker/',views.tracker,name='TrackingStatus'),
    path('Exchnage/',views.Exchange),
    path('Exchnage/sell/',views.Exchange_sell),
    path('Exchnage/buy/',views.Exchange_buy),
    path('Exchnage/buy/bookid=<int:id>/bookname=<str:search>/',views.Exchange_buy_item),
    path('Exchnage/Searches/',views.Searches),
    path('search/',views.search,name='Search'),
    path('products/<int:myid>',views.prodview,name='Productview'),
    path('checkout/',views.checkout,name='Checkout'),
    path('handlerequest/',views.handlereq,name='handlerequest'),
    
]
