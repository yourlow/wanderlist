from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matt/', views.matt, name='matt'),
    path('test/', views.matt, name='test'),
    path('<int:id>/brian/', views.brian, name='brian'),
    path('<str:business_name>/add_business/', views.add_business, name='example'),
    path('<int:business_id>/get_business_name/', views.get_business_by_id, name='get'),
]
