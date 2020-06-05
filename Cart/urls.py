from django.conf.urls import url

from Cart import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
    url(r'^addToCart/', views.addToCart),
    url(r'^subToCart/', views.subToCart),
    url(r'^changeStatus/', views.changestatus),
    url(r'^allselect/', views.allselect)
]