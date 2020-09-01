from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

def index(request):
   # template = loader.get_template('templates/base.html')
   #return render(request, "base.html")
    return HttpResponse("Hello world, you're at the wanderlist index, just a test")

def add_business(request, business_name, business_password):
    business_instance = Business.objects.create(name=business_name, password=business_password)
    return HttpResponse("added" + business_name)

def set_user(request, name, password, rank, instagram, facebook, twitter):
    new_user = User.objects.create(name=name, password=password, rank=rank)
    if (instagram):
        new_user.update(instagram=instagram)
    
    if (facebook):
        new_user.update(facebook=facebook)

    if (twitter):
        new_user.update(twitter=twitter)

    return HttpResponse("added" + name)

def update_user_name(request, id, new_name):
    update_user = User.objects.filter(id=id).update(name=new_name)
    return HttpResponse("new name is: " + new_name)

def get_business_by_id(request, business_id):
    get_activity = Business.objects.all().filter(id=business_id)
    return HttpResponse(get_activity)

def get_bucketlist_activities(request, bucketlist_id):
    bucketlist_activities = BucketList_Activity.objects.filter(bucketlist_id=bucketlist_id).values('activity_id')
    bucketlist_activities_list = list(bucketlist_activities)
    return JsonResponse(bucketlist_activities_list, safe=False)

def get_rewards(request, activity_id):
    rewards = Reward.objects.filter(activity_id=activity_id).values('id')
    rewards_list = list(rewards)
    return JsonResponse(rewards_list, safe=False)

def get_user_rewards(request, user_id, redeemed):
    # work out how to do booleans
    rewards = User_Rewards.objects.filter(user_id=user_id, redeemed=redeemed).values('id', 'reward_id')
    rewards_list = list(rewards)
    return JsonResponse(rewards_list, safe=False)

def get_specific_user_reward(request, user_id, reward_id):
    # seems weird, returns different ids 
    rewards = User_Rewards.objects.filter(user_id=user_id, reward_id=reward_id).values('id', 'reward_id')
    rewards_list = list(rewards)
    return JsonResponse(rewards_list, safe=False)

def get_business(request, id):
    business = Business.objects.filter(id=id).values('id','name')
    business_list = list(business)
    return JsonResponse(business_list, safe=False)

def get_all_business(request):
    business = Business.objects.all().values('id', 'name', 'password')
    business_list = list(business)
    return JsonResponse(business_list, safe=False)

def get_bucketlists(request, user_id):
    bucketlist = BucketList.objects.filter(user_id=user_id).values('id', 'name', 'user_id')
    bucketlist_list = list(bucketlist)
    return JsonResponse(bucketlist_list, safe=False)

def post_list(request, list_name, user_id):
    user = User.objects.get(id=user_id)
    new_list = BucketList.objects.create(name=list_name, user_id=user)
    return HttpResponse("added post list = " + list_name)

def get_activities(request):
    activities = Activity.objects.all().values()
    activities_list = list(activities)
    return JsonResponse(activities_list, safe=False)