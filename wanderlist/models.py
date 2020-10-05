from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class UserManager(BaseUserManager):
    def create_user(self, name, password=None):
        if name is None:
            raise TypeError('Not a valid username')
        user = self.model(name=name)
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, name, password=None):
        if password is None:
            raise TypeError('Not a valid password')

        user = self.create_user(name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# Models for the wanderlist app

class Business(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id) + ' ' + self.name


class Activity(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
    website = models.URLField(blank=True)
    video = models.URLField(blank=True)
    education = models.URLField(blank=True)
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.title


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    # email = models.EmailField(max_length=255, unique=True, db_index=True)
    rank = models.IntegerField(default=0)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    location = models.CharField(max_length=200, default='St Lucia QLD', blank=True)

    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return str(self.id) + ' ' + self.name

    # def tokens(self):
    #     return ''


class BucketList(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

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

    def __str__(self):
        return str(self.id) + ' BucketList: ' + str(self.bucketlist_id) + ' Activity: ' + str(self.activity_id)


class User_Activity(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' User: ' + str(self.user_id) + ' Activity: ' + str(self.activity_id)
