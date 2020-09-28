from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('post_list/<list_name>/<user_id>', views.post_list, name='post_list'),
    path('get_activity', views.get_activity, name="get_activity"),
    path('get_activity/<activity_id>', views.get_activity_specific, name="get_activity_specific"),
    path('add_activity_to_list/<list_id>/<activity_id>', views.add_activity_to_list, name="add_activity_to_list"),
    path('get_user/<user_id>', views.get_user, name="get_user"),
    path('get_user_rewards/<user_id>', views.get_user_rewards, name='get_user_rewards'),
    path('create_list/<name>/<user_id>', views.create_list, name='create_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)