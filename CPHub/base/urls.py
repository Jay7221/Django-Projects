from django.urls import path
from .views import PostCreate, PostDelete, PostDetail, PostList, PostUpdate

urlpatterns = [
    path('post-list', PostList.as_view(), name='post-list'),
    path('post-detail/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
    path('post-update/<int:pk>', PostUpdate.as_view(), name='post-update'),
    path('post-delete/<int:pk>', PostDelete.as_view(), name='post-delete'),
]
