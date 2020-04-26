from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=20, default='')
    password = models.CharField(max_length=40, default='')
    telegram_chat_id = models.CharField(max_length=100, default='')
    telegram_username = models.CharField(max_length=100, default='')
    profile_photo = models.CharField(max_length=400, blank=True, default='')
    faculty = models.CharField(max_length=50, blank=True, default='')
    gender = models.CharField(max_length=50, blank=True, default='')
    year_of_study = models.IntegerField(default=1, blank=True)
    registration_time = models.DateTimeField(auto_now_add=True)


class TeacherInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500, default='')
    quote = models.CharField(max_length=200, default='')
    is_teaching = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)


class Code(models.Model):
    code = models.CharField(max_length=6)
    is_valid = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    telegram_chat_id = models.IntegerField(default=1)
    telegram_username = models.CharField(default='', max_length=20)
