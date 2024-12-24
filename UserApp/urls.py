from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , index , name="home"),
    path("login/" , loginpage , name='loginpage'),
    path("signup/" , singup , name="signup"),
    path("profile/" , profile , name="profile"),
    path("message/" , messages , name="message"),
    path("notify" , Notiy , name="notify"),
    path("upload_reel" , upload_reel , name="upload_reel"),
    path("upload_post" , upload_post , name="upload_post"),
    path("explore" , explore , name="explore"),
    path("logout" , logoutpage , name="logout" ),
    path('UploadStory' , UploadStory,  name="UploadStory"),
    path("userprofile/<int:id>" , userprofile , name="userprofile"),
    path("save<int:id>" , save , name='save'),
    path("follow/<int:id>" , Follow , name="follow"),
    path("unfollow/<int:id>" , unfollow , name="unfollow"),
    path('like/<int:id>' , LikePost , name='like'),
    path('hastage/<int:id>' , HasTageView , name="hastage"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)