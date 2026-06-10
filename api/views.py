from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from api.models import Post
from api.serializers import PostSerializer


# def salom(request):
#     return  JsonResponse({'massage':'Hello DRF'})


class PostListCreateAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer_class = PostSerializer
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request,pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


