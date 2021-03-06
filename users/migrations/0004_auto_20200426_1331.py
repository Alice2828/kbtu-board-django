# Generated by Django 3.0.4 on 2020-04-26 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200425_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='telegram_chat_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='code',
            name='telegram_username',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='quote',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='subject',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='faculty',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_chat_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram_username',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
