from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.contact_form,name='contact_insert'),
    path('<int:id>/',views.contact_form,name='contact_update'),
    path('delete/<int:id>/',views.contact_delete,name='contact_delete'),
    path('list/', views.contact_list,name='contact_list')
]