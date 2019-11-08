from django.urls import path
from blog import views

urlpatterns = [
    path('config/load-data', views.load_json),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),    
    path('profiles/', views.ProfileList.as_view(), name=views.ProfileList.name),
    path('profiles/<int:pk>', views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
    path('posts/', views.PostList.as_view(), name=views.PostList.name),
    path('posts/<int:pk>', views.PostDetail.as_view(), name=views.PostDetail.name),
    path('comments/', views.CommentList.as_view(), name=views.CommentList.name),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name=views.CommentDetail.name),
    path('profile-posts/', views.ProfilePostList.as_view(), name=views.ProfilePostList.name),
    path('profile-posts/<int:pk>', views.ProfilePostDetail.as_view(), name=views.ProfilePostDetail.name),
]