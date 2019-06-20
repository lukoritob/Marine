from django.urls import path
from . import views

app_name = 'sea'
urlpatterns = [
    path('', views.index, name='index'),

    path('yote', views.records, name='yote'),
    path('think', views.query2, name='think'),
    path('stuffs', views.query3, name='stuffs'),
    path('lastone', views.query13, name='lastone'),
    path('input', views.query4, name='input'),
    path('input1', views.query5, name='input1'),
    path('input2', views.query6, name='input2'),
    path('input3', views.query7, name='input3'),
    path('input4', views.query8, name='input4'),
    path('input5', views.query9, name='input5'),
    path('input6', views.query10, name='input6'),
    path('input7', views.query11, name='input7'),
    path('delete', views.query12, name='delete')
]