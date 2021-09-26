from rest_framework import serializers
from rest_framework.utils import field_mapping
from django.contrib.auth.models import User

from web.models import Comment, Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username')


class UserSerializerWithToken(serializers.ModelSerializer):
    
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['heading', 'description','photo','id','comments','no']
    
    def get_comments(self, obj):
        return obj.comments_count()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('post','comment')


