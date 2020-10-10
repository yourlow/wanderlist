from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    ## these are gets and posts for all our models
    path('business/', views.BusinessList.as_view()),
    path('activity/', views.ActivityList.as_view()),
    path('user/', views.UserList.as_view()),
    path('bucketlist/', views.BucketListList.as_view()),
    path('rewards/', views.RewardList.as_view()),
    path('user_rewards/', views.User_RewardsList.as_view()),
    path('bucketlist_activity/', views.BucketList_ActivityList.as_view()),
    path('user_activity/', views.User_ActivityList.as_view()),
    path('location/', views.LocationList.as_view()),

    ## get/put/patch requests
    path('business/<int:id>/', views.BusinessDetail.as_view()),
    path('activity/<int:id>/', views.ActivityDetail.as_view()),
    path('user/<int:id>/', views.UserDetail.as_view()),
    path('bucketlist/<int:id>/', views.BucketListDetail.as_view()),
    path('rewards/<int:id>/', views.RewardDetail.as_view()),
    path('user_rewards/<int:id>', views.User_RewardsDetail.as_view()),
    path('bucketlist_activity/<int:id>/', views.BucketList_ActivityDetail.as_view()),
    path('user_activity/<int:id>/', views.User_ActivityDetail.as_view()),

    ## custom views
    path('get_bucketlist_activities/<int:id>/', views.GetBucketlistActivities.as_view()),
    path('get_reward/<int:id>/', views.GetRewards.as_view()),
    path('get_user_rewards/<int:id>/<redeemed>/', views.GetUserRewards.as_view()),
    path('get_specific_user_rewards/<int:user_id>/<int:reward_id>/', views.GetSpecificUserRewards.as_view()),
    path('get_specific_activity/<int:id>/', views.GetSpecificActivity.as_view()),
    path('complete_activity/', views.CompleteActivity.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)