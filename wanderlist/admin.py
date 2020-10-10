from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *
"""
class BusinessAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

class ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

class BucketListAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

class RewardAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

class User_RewardsAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

class User_ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

class BucketList_ActivityAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
"""
#models = [Business, Activity, User, BucketList, Reward, User_Rewards, User_Activity, BucketList_Activity, BusinessAdmin, ActivityAdmin, UserAdmin, BucketListAdmin, RewardAdmin, User_RewardsAdmin, User_ActivityAdmin, BucketList_ActivityAdmin]
models = [Business, Location, Activity, User, BucketList, Reward, User_Rewards, User_Activity, BucketList_Activity]
admin.site.register(models)