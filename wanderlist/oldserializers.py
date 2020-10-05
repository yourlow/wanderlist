# class ActivitySerializer(serializers.Serializer):
#     latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
#     longitude = serializers.DecimalField(max_digits=9, decimal_places=6)
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=200)
#     points = serializers.IntegerField(default=0)
#     website = serializers.URLField(allow_blank=True)
#     video = serializers.URLField(allow_blank=True)    
#     education = serializers.URLField(allow_blank=True)

#     tags = serializers.CharField(max_length=200, allow_blank=True)

#     def __str__(self):
#         return str(self.id) + ' ' + self.title

#     def create(self, validated_data):
#         return Activity.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.latitude = validated_data.get('latitude', instance.latitude)
#         instance.longitude = validated_data.get('longitude', instance.longitude)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.points = validated_data.get('points', instance.points)
#         instance.website = validated_data.get('website', instance.website)
#         instance.video = validated_data.get('video', instance.video)
#         instance.education = validated_data.get('education', instance.education)
#         instance.tags = validated_data.get('tags', instance.tags)
#         instance.save()
#         return instance

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    rank = serializers.IntegerField(default=0)
    instagram = serializers.URLField(allow_blank=True)
    facebook = serializers.URLField(allow_blank=True)
    twitter = serializers.URLField(allow_blank=True)
    location = serializers.CharField(max_length=200, default='St Lucia QLD', allow_blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.name

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.rank = validated_data.get('rank', instance.rank)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.twitter = validated_data.get('twitter', instance.twitter)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance

class BucketListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' User: ' + str(self.user_id) 
    
    def create(self, validated_data):
        return BucketList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class RewardSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200, allow_blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.name
    
    def create(self, validated_data):
        return Reward.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
    
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class User_RewardsSerializer(serializers.Serializer):
    redeemed = serializers.BooleanField()

    def __str__(self):
        return str(self.id) + ' Reward: ' + str(self.reward_id) + ' User: ' + str(self.user_id)

    def create(self, validated_data):
        return User_Rewards.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.redeemed = validated_data.get('redeemed', instance.redeemed)
        instance.save()
        return instance

class BucketList_ActivitySerializer(serializers.Serializer):
    completed = serializers.BooleanField()
    
    def __str__(self):
        return str(self.id) + ' BucketList: ' + str(self.bucketlist_id) + ' Activity: ' + str(self.activity_id)
    
    def create(self, validated_data):
        return BucketList_Activity.objects.create(**validated_data)

    def update(self, instance, validated_data):
    
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance

class User_ActivitySerializer(serializers.Serializer):
    def create(self, validated_data):
        return User_Activity.objects.create(**validated_data)

        
class BusinessSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' ' + self.name

    def create(self, validated_data):
        return Business.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance