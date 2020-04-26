from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    telegram_chat_id = models.CharField(max_length=100)
    telegram_username = models.CharField(max_length=100)
    profile_photo = models.CharField(max_length=400, blank=True)
    faculty = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    year_of_study = models.IntegerField(default=1, blank=True)
    registration_time = models.DateTimeField(auto_now_add=True)


class TeacherInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500)
    quote = models.CharField(max_length=200)
    is_teaching = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)


class Code(models.Model):
    code = models.CharField(max_length=6)
    is_valid = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True)
