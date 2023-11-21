from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('page2/',page2,name='page2'),
]