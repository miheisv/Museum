from django.urls import path, re_path

from . import views

app_name = 'homepage'

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),
    path(
        'create_post/',
        views.CreatePostView.as_view(),
        name='create_post'
    ),
    path(
        'news/',
        views.PostListView.as_view(),
        name='news'
    ),
    
    re_path(
        r'^post/(?P<pk>[1-9][0-9]*)/$',
        views.PostView.as_view(),
        name='post'
    ),
]
