from django.urls import path, re_path
from . import views
# from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    re_path(r'^search/', views.search_results, name='search_results'),
    path('upload/', views.upload, name='upload'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    # path('post/<int:image_id>/like',views.like_image,name='likeimage'),
    re_path(r'^like/(?P<operation>.+)/(?P<pk>\d+)/',views.like_image, name='like'),
    # path('logout/', views.logout, name='logout'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)