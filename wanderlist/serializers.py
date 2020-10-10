from rest_framework import serializers
from wanderlist.models import *

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList
        fields = '__all__'

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = '__all__'

class User_RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Rewards
        fields = '__all__'

class BucketList_ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList_Activity
        fields = '__all__'

class User_ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Activity
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'