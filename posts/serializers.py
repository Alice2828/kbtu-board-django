from datetime import datetime

from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    # creation_date = serializers.DateField(format="%Y-%m-%d")
    # user_id = serializers.IntegerField(default=0)
    # time = serializers.TimeField(format="%H:%M:%S")
    # place = serializers.CharField(default='')
    # photo = serializers.CharField(default='')
    # category_id = serializers.IntegerField(default=1)

    class Meta:
        model = Post
        fields = '__all__'
    # def create(self, validated_data):
    #     post = Post.objects.create(title=validated_data.get('title'),
    #                                description=validated_data.get('description'),
    #                                creation_date=validated_data.get('creation_date'),
    #                                user_id=validated_data.get('user_id'),
    #                                time=validated_data.get('time'),
    #                                place=validated_data.get('place'),
    #                                photo=validated_data.get('photo'),
    #                                category_id=validated_data.get('category_id'))
    #     return post
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance
