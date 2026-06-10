from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView

urlpatterns = [
    # path('api/hello/', salom),
    path('api/v1/posts/list-create/', PostListCreateAPIView.as_view()),
    path('api/v1/posts/detail/<int:pk>/', PostDetailAPIView.as_view()),

]