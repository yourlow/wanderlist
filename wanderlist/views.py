from wanderlist.models import *
from wanderlist.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

def index(request):
    #return HttpResponse('Refer to onedrive Routes document for details on routes')
    template = loader.get_template('wanderlist/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

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
        activity = self.get_object(id)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

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
        bucketlist = self.get_object(id)
        serializer = BucketListSerializer(bucketlist)
        return Response(serializer.data)

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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
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