from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from posts.views import (PostCreateView, PostDeleteView, PostDetailView,
                         PostListView, PostUpdateView)

from .views import CustomLoginView, CustomLogoutView, CustomRegisterView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('create_content/', PostListView.as_view(), name='create_content'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
