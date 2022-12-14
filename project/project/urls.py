from django.urls import path
from polls import views

urlpatterns = [
    path('', views.styl),
    path('appointment', views.post),

    # 2 задание

    # path('index', views.index),
    # path('form', views.post1)
]
