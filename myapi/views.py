from django.shortcuts import render
from web.models import Post,Comment, User
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, permission_classes, renderer_classes,authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from myapi.serializers import PostSerializer,CommentSerializer
from rest_framework import status
from django.contrib.auth.models import User
# from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework.views import APIView


# @api_view(['GET'])
# def current_user(request):
#     """
#     Determine the current user by their token, and return their data
#     """
    
#     serializer = UserSerializer(request.user)
#     return Response(serializer.data)


# @permission_classes((IsAuthenticated,))
@api_view(['GET'])
def user_list(self, request, format=None):
    serializer = UserSerializerWithToken(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def posts(request):
    instances = Post.objects.all().order_by("-id")
    serialized = PostSerializer(instances,many=True,context={"request":request})
    
    response_data = {
        "StatusCode" : 6000,
        'data' : serialized.data
    }

    return Response(response_data, status=status.HTTP_200_OK)



@api_view(['POST'])
@renderer_classes((JSONRenderer,))
# @permission_classes((IsAuthenticated,))
def new_posts(request):
    serializer = PostSerializer(data=request.data,context={"request":request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@renderer_classes((JSONRenderer,))
# @permission_classes((IsAuthenticated,))
def comments(request):
    instances = Comment.objects.all().order_by("id")
    serialized = CommentSerializer(instances,many=True,context={"request":request})

    response_data = {
        "StatusCode" : 6000,
        'data' : serialized.data
    }

    return Response(response_data, status=status.HTTP_200_OK)



@api_view(['POST'])
@renderer_classes((JSONRenderer,))
# @permission_classes((IsAuthenticated,))
def new_comments(request):
    serializer = CommentSerializer(data=request.data,context={"request":request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)