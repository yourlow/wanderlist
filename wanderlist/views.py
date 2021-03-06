from wanderlist.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
from django.http import HttpResponse
import json

def index(request):
    #return HttpResponse('Refer to onedrive Routes document for details on routes')
    template = loader.get_template('wanderlist/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


class LocationList(APIView):
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class BusinessList(APIView):
    def get(self, request, format=None):
        businesses = Business.objects.all()
        serializer = BusinessSerializer(businesses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class BusinessDetail(APIView):
    def get_object(self, id):
        try:
            return Business.objects.get(id=id)
        except Business.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        business = self.get_object(id)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        business = self.get_object(id)
        serializer = BusinessSerializer(business, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        business = self.get_object(id)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        business = self.get_object(id)
        serializer = BusinessSerializer(business, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivityList(APIView):
    def get(self, request, format=None):
        activity = Activity.objects.all()
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class ActivityDetail(APIView):
    def get_object(self, id):
        try:
            return Activity.objects.get(id=id)
        except Activity.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        activity = list(Activity.objects.filter(id=id).values())
        activity[0]['sustainability_rating'] = Activity.objects.get(id=id).avg_sustainability_rating
        activity[0]['fun_rating'] = Activity.objects.get(id=id).avg_fun_rating
        return Response(activity)

    def put(self, request, id, format=None):
        activity = self.get_object(id)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        activity = self.get_object(id)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        activity = self.get_object(id)
        serializer = ActivitySerializer(activity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        user = self.get_object(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        user = self.get_object(id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BucketListList(APIView):
    def get(self, request, format=None):
        bucket_list = BucketList.objects.all()
        serializer = BucketListSerializer(bucket_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BucketListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class BucketListDetail(APIView):
    def get_object(self, id):
        try:
            return BucketList.objects.get(id=id)
        except BucketList.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        bucketlist = list(BucketList.objects.filter(id=id).values())
        bucketlist[0]['activity_count'] = BucketList_Activity.objects.filter(bucketlist_id=id).count()
        return Response(bucketlist)

    def put(self, request, id, format=None):
        bucketlist = self.get_object(id)
        serializer = BucketListSerializer(bucketlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        bucketlist = self.get_object(id)
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        bucketlist = self.get_object(id)
        serializer = BucketListSerializer(bucketlist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RewardList(APIView):
    def get(self, request, format=None):
        reward = Reward.objects.all()
        serializer = RewardSerializer(reward, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class RewardDetail(APIView):
    def get_object(self, id):
        try:
            return Reward.objects.get(id=id)
        except Reward.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        reward = self.get_object(id)
        serializer = RewardSerializer(reward)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        reward = self.get_object(id)
        serializer = RewardSerializer(reward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        reward = self.get_object(id)
        reward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        reward = self.get_object(id)
        serializer = RewardSerializer(reward, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User_RewardsList(APIView):
    def get(self, request, format=None):
        user_rewards = User_Rewards.objects.all()
        serializer = User_RewardsSerializer(user_rewards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = User_RewardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class User_RewardsDetail(APIView):
    def get_object(self, id):
        try:
            return User_Rewards.objects.get(id=id)
        except User_Rewards.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user_reward = self.get_object(id)
        serializer = User_RewardsSerializer(user_reward)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user_reward = self.get_object(id)
        serializer = User_RewardsSerializer(user_reward, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user_reward = self.get_object(id)
        user_reward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        user_rewards = self.get_object(id)
        serializer = User_RewardsSerializer(user_rewards, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BucketList_ActivityList(APIView):
    def get(self, request, format=None):
        bucket_list_activity = BucketList_Activity.objects.all()
        serializer = BucketList_ActivitySerializer(bucket_list_activity, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BucketList_ActivitySerializer(data=request.data)
        if serializer.is_valid():
            bucketlist = list(BucketList_Activity.objects.filter(bucketlist_id=request.data['bucketlist_id'],
                                                                 activity_id=request.data['activity_id']).values())
            if not bucketlist:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class BucketList_ActivityDetail(APIView):
    def get_object(self, id):
        try:
            return BucketList_Activity.objects.get(id=id)
        except BucketList_Activity.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        bucketlist_activity = self.get_object(id)
        serializer = BucketList_ActivitySerializer(bucketlist_activity)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        bucketlist_activity = self.get_object(id)
        serializer = BucketList_ActivitySerializer(bucketlist_activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        bucketlist_activity = self.get_object(id)
        bucketlist_activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        bucketlist_activity = self.get_object(id)
        serializer = BucketList_ActivitySerializer(bucketlist_activity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class User_ActivityList(APIView):
    def get(self, request, format=None):
        user_activity_list = User_Activity.objects.all()
        serializer = User_ActivitySerializer(user_activity_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = User_ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class User_ActivityDetail(APIView):
    def get_object(self, id):
        try:
            return User_Activity.objects.get(id=id)
        except User_Activity.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        user_activity = self.get_object(id)
        serializer = User_ActivitySerializer(user_activity)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        user_activity = self.get_object(id)
        serializer = User_ActivitySerializer(user_activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        user_activity = self.get_object(id)
        user_activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        user_activity = self.get_object(id)
        serializer = User_ActivitySerializer(user_activity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#return all reward data
class GetUserRewards(APIView):
    def get_reward_object(self, id):
        try:
            return Reward.objects.get(id=id)
        except Reward.DoesNotExist:
            raise Http404

    def get_object(self, id):
        try:
            return User_Rewards.objects.get(id=id)
        except User_Rewards.DoesNotExist:
            raise Http404
    
    def get(self, request, id, format=None):
        user_reward = self.get_object(id)
        user_reward_serializer = User_RewardsSerializer(user_reward)
        reward_id = user_reward_serializer.data['reward_id']
        print(reward_id)
        reward = self.get_reward_object(reward_id)
        reward_serializer = RewardSerializer(reward)
        print(reward_serializer.data)
        return Response(reward_serializer.data)

    def put(self, request, id, format=None):
        activity = self.get_object(id)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        activity = self.get_object(id)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetBucketlistActivities(APIView):
    def get_object(self, id):
        try:
            return BucketList_Activity.objects.get(id=id)
        except BucketList_Activity.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        bucketlist_activities = list(
            BucketList_Activity.objects.filter(bucketlist_id=id).values('activity_id', 'completed', 'sustainability_rating', 'fun_rating'))
        for activity in bucketlist_activities:
            activity.update(list(
                Activity.objects.filter(id=activity['activity_id']).values('title', 'location', 'tags'))[
                                0])
            activity.update(list(Location.objects.filter(id=activity['location']).values('latitude', 'longitude'))[0])
            activity['avg_sustainability_rating'] = Activity.objects.get(id=activity['activity_id']).avg_sustainability_rating
            activity['avg_fun_rating'] = Activity.objects.get(id=activity['activity_id']).avg_fun_rating

        return Response(bucketlist_activities)

class GetRewards(APIView):
    def get_object(self, id):
        try:
            return Reward.objects.get(id=id)
        except Reward.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        rewards = Reward.objects.filter(activity_id=id).values('id')
        rewards_list = list(rewards)
        return Response(rewards_list)

class GetUserRewards(APIView):
    def get_object(self, id):
        try:
            return User_Rewards.objects.get(id=id)
        except User_Rewards.DoesNotExist:
            raise Http404

    def get(self, request, id, redeemed, format=None):
        # work out how to do booleans
        rewards = User_Rewards.objects.filter(user_id=id, redeemed=redeemed).values('id', 'reward_id')
        rewards_list = list(rewards)
        return Response(rewards_list)

class GetSpecificUserRewards(APIView):
    def get_object(self, id):
        try:
            return User_Rewards.objects.get(id=id)
        except User_Rewards.DoesNotExist:
            raise Http404

    def get(self, request, user_id, reward_id, format=None):
        # seems weird, returns different ids
        rewards = User_Rewards.objects.filter(user_id=user_id, reward_id=reward_id).values('id', 'reward_id')
        rewards_list = list(rewards)
        return Response(rewards_list)

class GetActivityByLocationID(APIView):
    def get(self, request, location_id):
        activities = Activity.objects.filter(location=location_id).values()
        for activity in activities:
            activity['sustainability_rating'] = Activity.objects.get(id=activity['id']).avg_sustainability_rating
            activity['fun_rating'] = Activity.objects.get(id=activity['id']).avg_fun_rating
        return Response(list(activities))

class GetSpecificActivity(APIView):
    def get_object(self, id):
        try:
            return Activity.objects.get(id=id)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        activities = list(Activity.objects.filter(id=id).values())
        activities[0]['sustainability_rating'] = Activity.objects.get(id=id).avg_sustainability_rating
        activities[0]['fun_rating'] = Activity.objects.get(id=id).avg_fun_rating
        return Response(activities)

class GetBucketlistBelongToUser(APIView):
    def get(self, request, user_id):
        bucketlist = BucketList.objects.filter(user_id=user_id).values()
        for bucket in bucketlist:
            bucket['activity_count'] = BucketList_Activity.objects.filter(bucketlist_id=bucket['id']).count()
        return Response(list(bucketlist))

class GetAllUserRewards(APIView):
    def get(self, request, user_id):
        user_rewards = list(User_Rewards.objects.filter(user_id=user_id).values())
        for user_reward in user_rewards:
            user_reward.update(list(Reward.objects.filter(id=user_reward['reward_id_id']).values())[0])
        return Response(user_rewards)

class SimpleLogin(APIView):
    def get(self, request, username, password):
        try:
            user = User.objects.filter(name=username).values()
            if 'id' not in user[0]:
                return Response(status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(status.HTTP_401_UNAUTHORIZED)

        if user[0]['password'] == password:
            return Response(list(user))
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)

class CompleteActivity(APIView):
    def post(self, request):
        data = request.data
        try:
            activity = Activity.objects.get(id=int(data['activity_id']))
        except:
            return Response("activity does not exist")
        
        if(int(data['qr_code']) != activity.id):
            return Response("qr codes do not match")
       
        user_activity = User_Activity.objects.filter(user_id=int(data['user_id']), activity_id=int(data['activity_id'])).count()
        bucketlist = BucketList_Activity.objects.filter(bucketlist_id=int(data['bucketlist_id']), activity_id=int(data['activity_id'])).update(completed = 1)
            
        if(user_activity):
            return Response("already completed")
    
        serializer = User_ActivitySerializer(data=data)
      
        if serializer.is_valid() :
            serializer.save()
            reward = Reward.objects.filter(activity_id = int(data['activity_id']))
            
            if(not reward.exists()):
                return Response("-1", status=status.HTTP_201_CREATED)
            
            reward = list(reward.values())[0]
            reward_serializer = User_RewardsSerializer(data = {'reward_id':reward["id"], 'user_id' :int(data['user_id']), 'redeemed' : False} )
        
            if(reward_serializer.is_valid()):
                reward_serializer.save()
            return Response(reward["name"], status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class RateActivity(APIView):
    def post(self, request):
        data = request.data
        try:
            BucketList_Activity.objects.filter(bucketlist_id=int(data['bucketlist_id']), activity_id=int(data['activity_id'])).update(sustainability_rating=data['sustainability_rating'], fun_rating=data['fun_rating'])
            return Response("Rating successful")
        except:
            return Response("This activity hasn't been completed")