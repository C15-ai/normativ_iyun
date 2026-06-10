from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=True)
    class Meta:
        model = Post
        fields = ('title' , 'content')


    def validate_title(self, value):

        if not value.strip():
            raise serializers.ValidationError("Title bo'sh bo'lmasligi kerak")
        return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Content 10 ta strdan kop bolishi shart")
        return value


