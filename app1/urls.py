from django.urls import path
from .views import  HomePage,VacationPage,DetailPage,EditPage,DeletePage,CreatePage, URLshorten


urlpatterns=[
    path('',HomePage, name='home'),
    path('/Job', VacationPage, name='vacation'),
    path('/Job/create', CreatePage, name='create'),
    path('/Job/detail/<int:pk>', DetailPage, name='detail'),
    path('/Job/detail/<int:pk>/edit',EditPage,name='edit'),
    path('/Job/detail/<int:pk>/delete',DeletePage,name='delete'),
    path('service/', URLshorten, name = 'urlshort')

]