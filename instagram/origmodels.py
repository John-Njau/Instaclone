# from django.db import models
# from django.contrib.auth.models import User


# # Create your models here.
# class Profile(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="image")
#     bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
#     profilepic = models.ImageField(upload_to='uploads/profilepics/', null=True, blank=True)
#     # followers = models.ManyToManyField(User, related_name="followers", blank=True)
#     # following = models.ManyToManyField(User, related_name="following", blank=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_created = models.DateTimeField(auto_now=True)
    
#     def updateprofile(self,name):
#         self.name = name
#         self.save()
        
#     @classmethod
#     def search_profiles(cls,search_term):
#         profiles = cls.objects.filter(user__icontains=search_term)
#         return profiles
    
#     def __str__(self)-> str:
#         return f'{self.user.username}'
    
# class Image(models.Model):
#     image=models.ImageField(upload_to='uploads/gramposts/', )
#     name = models.CharField(max_length=30)
#     caption=models.TextField()
#     uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
#     # likes = models.ManyToManyField('Profile', related_name='likes')
#     # comments = models.ManyToManyField('Profile', related_name='comments', null=True, blank=True)
#     date_uploaded = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         verbose_name_plural = ('images')
    
#     def save_image(self):
#         self.save()
        
#     def delete_image(self):
#         self.delete()
        
#     def update_caption(self):
#         self.save()
        
#     @classmethod
#     def search_by_name(cls, search_term):
#         results = cls.objects.filter(name__icontains=search_term)
#         return results

#     def __str__(self):
#         return self.name
    
    
# class Comments (models.Model):
#     comment = models.CharField(max_length=255)
#     comment_by = models.ForeignKey('Profile',related_name='uploaded_by' , on_delete=models.CASCADE)
#     image_commented_on = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='images')
#     comment_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.comment
    
#     class Meta:
#         verbose_name_plural = ('comments')
    
    
# # class Likes(models.Model):
# #     liked_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image_likes')
# #     liked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

    
# #     class Meta:
# #         verbose_name_plural = ('likes')
        
# #     def __str__(self) -> str:
# #         return f"{self.user.username}"

# class Follow(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
#     following = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='follow', null=True)
#     follower = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='follower', null=True)

#     def __str__(self) -> str:
#         return f"{self.follower}"