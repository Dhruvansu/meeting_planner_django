from django.urls import path
from . import views

urlpatterns =[
    path('/<int:id>', views.room_detail, name="room_detail"),
    path('', views.room_list, name="rooms_list"),
]