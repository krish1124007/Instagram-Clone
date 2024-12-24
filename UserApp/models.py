from django.db import models
from django.contrib.auth.models import User
# Create your models here.         


class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     profile_image = models.ImageField( upload_to='Profile_image', height_field=None, width_field=None, max_length=None , default='https://th.bing.com/th/id/OIP.DzBlyLi5oo0RCww-wose6wAAAA?rs=1&pid=ImgDetMain')
     profile_bio = models.CharField(max_length=50 , null=True)
     privet_account = models.BooleanField(null=True , default=False)



class Post(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     hastage=  models.TextField(null=True)
     post_img = models.FileField( upload_to='UserPost', max_length=100)
     caption = models.CharField( max_length=200)
     created_on = models.DateTimeField(auto_now_add=True)
     updated_on = models.DateTimeField(auto_now_add=True)



    
class Like(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     post = models.ForeignKey(Post, on_delete=models.CASCADE)
     created_on = models.DateTimeField(auto_now_add=True)
     updated_on = models.DateTimeField(auto_now_add=True)

     class Meta:
         unique_together = ('user' , 'post')


    
class Followed(models.Model):
     follower = models.ForeignKey(User , related_name='follower', on_delete=models.CASCADE , null=True)
     following = models.ForeignKey(User , related_name='following' , on_delete=models.CASCADE , null=True)
     created_on = models.DateField(null=True, auto_now=False, auto_now_add=False)
     
     class Meta:    
        unique_together = ('follower', 'following')

     def __str__(self):
        return f'{self.following} follows {self.follower}'
     



class Notification(models.Model):
    ToMessage = models.ForeignKey(User, on_delete=models.CASCADE , related_name='ToMessage')
    Message = models.CharField(max_length=200)
    FromMessage = models.ForeignKey(User, on_delete=models.CASCADE , null=True , related_name='FromMessage')





class  Save(models.Model):
     user = models.ForeignKey(User , on_delete=models.CASCADE)
     post = models.ForeignKey(Post, related_name='post' , on_delete=models.CASCADE , null=True)
     created_on = models.DateTimeField(auto_now_add=True)
     updated_on = models.DateTimeField(auto_now_add=True)

     class Meta:    
        unique_together = ('user', 'post')



class Story(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    story = models.FileField(upload_to='Story', max_length=100)
    created_on = models.TimeField(auto_now_add=True)