from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=True)
    class Meta:
        model = Post
        fields = ('id' , 'title' , 'content')


    def validate_title(self, value):

        if not value.strip():
            raise serializers.ValidationError("Title bo'sh bo'lmasligi kerak")
        return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Content 10 ta strdan kop bolishi shart")
        return value





class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwordlar mos emas")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user