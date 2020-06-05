from django.conf.urls import url

from User import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^checkName/', views.checkName, name='checkName'),
    url(r'^send_mail/', views.send_email, name='send_email'),
    url(r'^account/', views.account, name='account'),
    url(r'^get_code/', views.get_code, name='get_code'),
    url(r'^loggout/', views.logout, name='logout')

]
