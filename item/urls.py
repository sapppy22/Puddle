from django.urls import path

from . import views

app_name='item'

urlpatterns=[
    path('',views.items,name='items'),
    path('new/',views.new,name='new'),
    path('detail/<int:pk>/',views.detail,name='detail'),
    path('detail/<int:pk>/delete/',views.delete,name='delete'),
    path('detail/<int:pk>/edit/',views.edit,name='edit'),
]