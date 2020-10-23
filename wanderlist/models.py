from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.db.models import Avg

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

#Models for the wanderlist app

class Location(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    imageurl = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.id) + ' Location: ' + str(self.name)

class Business(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' ' + self.name

class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    website = models.URLField(blank=True)
    video = models.URLField(blank=True)    
    education = models.URLField(blank=True)
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True)
    imageurl = models.CharField(max_length=200, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=300, null=True, blank=True)
    sustainable_description = models.CharField(max_length=300, null=True, blank=True)
    guidance_description = models.CharField(max_length=300, null=True, blank=True)

    def _get_sustainability_rating(self):
        return BucketList_Activity.objects.filter(activity_id=self.id).aggregate(avg_s_rating=Avg('sustainability_rating'))['avg_s_rating']
    avg_sustainability_rating = property(_get_sustainability_rating)

    def _get_fun_rating(self):
        return BucketList_Activity.objects.filter(activity_id=self.id).aggregate(avg_f_rating=Avg('fun_rating'))['avg_f_rating']
    avg_fun_rating = property(_get_fun_rating)
    
    def __str__(self):
        return str(self.id) + ' ' + self.title

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    location = models.CharField(max_length=200, default='St Lucia QLD', blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    def __str__(self):
        return str(self.id) + ' ' + self.name

class BucketList(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self): 
        return str(self.id) + ' ' + self.name + ' User: ' + str(self.user_id) 

class Reward(models.Model):
    name = models.CharField(max_length=200)
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.name

class User_Rewards(models.Model):
    reward_id = models.ForeignKey(Reward, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    redeemed = models.BooleanField()

    def __str__(self):
        return str(self.id) + ' Reward: ' + str(self.reward_id) + ' User: ' + str(self.user_id)

class BucketList_Activity(models.Model):
    bucketlist_id = models.ForeignKey(BucketList, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    completed = models.BooleanField()
    sustainability_rating = models.IntegerField(default=0)
    fun_rating = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id) + ' BucketList: ' + str(self.bucketlist_id) + ' Activity: ' + str(self.activity_id)

class User_Activity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' User: ' + str(self.user_id) + ' Activity: ' + str(self.activity_id)

