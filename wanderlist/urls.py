from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_bucketlist_activities/<bucketlist_id>', views.get_bucketlist_activities, name='get_bucketlist_activities'),
    path('get_rewards/<activity_id>', views.get_rewards, name='get_rewards'),
    path('get_user_rewards/<user_id>/<redeemed>', views.get_user_rewards, name='get_user_rewards'),
    path('get_specific_user_rewards/<user_id>/<reward_id>', views.get_specific_user_reward, name='get_specific_user_rewards'),
    path('get_business/<id>', views.get_business, name='get_business'),
    path('get_all_business', views.get_all_business, name='get_all_business'),
    path('set_user/<name>/<password>/<rank>/<instagram>/<facebook>/<twitter>', views.set_user, name='set_user'),
    path('update_user_name/<id>/<new_name>', views.update_user_name, name='update_user_name'),
    path('get_bucketlists/<user_id>', views.get_bucketlists, name='get_bucketlists'),
]
