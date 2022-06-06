from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    profilepic = models.ImageField(upload_to='uploads/profilepics/', null=True, blank=True)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def updateprofile(self,name):
        self.name = name
        self.save()
        
    @classmethod
    def search_profiles(cls,search_term):
        profiles = cls.objects.filter(user__icontains=search_term)
        return profiles
    
    def __str__(self):
        return self.profile.user
    
class Image(models.Model):
    image=models.ImageField(upload_to='uploads/gramposts/', )
    name = models.CharField(max_length=30, null=True, blank=True)
    caption=models.TextField()
    uploader_profile = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    likes = models.ManyToManyField('Profile', blank=True, related_name='likes')
    comments = models.ManyToManyField('Profile', related_name='comments')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_caption(self):
        self.save()
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = ('images')

    
    
class Comments (models.Model):
    comment = models.CharField(max_length=255)
    comment_by = models.ForeignKey('Profile',related_name='comment' , on_delete=models.CASCADE)
    image_commented_on = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='images')
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name_plural = ('comments')


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return self.email