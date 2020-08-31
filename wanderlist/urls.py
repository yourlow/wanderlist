from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('matt/', views.matt, name='matt'),
    path('test/', views.matt, name='test'),
    path('<int:id>/brian/', views.brian, name='brian'),
    path('<str:business_name>/add_business/', views.add_business, name='example'),
    path('<int:business_id>/get_business_name/', views.get_business_by_id, name='get'),
    path('get_bucketlist_activities/<bucketlist_id>', views.get_bucketlist_activities, name='get_bucketlist_activities'),
    path('get_rewards/<activity_id>', views.get_rewards, name='get_rewards'),
    path('get_user_rewards/<user_id>/<redeemed>', views.get_user_rewards, name='get_user_rewards'),
    path('get_specific_user_rewards/<user_id>/<reward_id>', views.get_specific_user_reward, name='get_specific_user_rewards'),
    path('get_business/<id>', views.get_business, name='get_business'),
]