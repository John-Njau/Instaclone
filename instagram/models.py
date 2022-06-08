from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, null=True, blank=True, default="bio")
    profilepic = models.ImageField(upload_to='uploads/profilepics/', null=True, blank=True)
    # followers = models.ManyToManyField(User, related_name="followers")
    # following = models.ManyToManyField(User, related_name="following")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def save_profile(self):
        self.save()

    # update profile
    def delete_profile(self, name):
        self.delete()

    def updateprofile(self, new_profile):
        self.profile = new_profile
        self.save()

    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def search_profiles(cls, search_term):
        profiles = cls.objects.filter(user__icontains=search_term)
        return profiles

    def __str__(self):
        return f'{self.user.username}'


class Image(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploader', null=True)
    # uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/gramposts/', )
    name = models.CharField(max_length=30)
    caption = models.TextField()
    likes = models.IntegerField('Likes', null=True)
    comments = models.ManyToManyField('Comments', related_name='comments')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_uploaded',)
        verbose_name_plural = ('images')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    @classmethod
    def search_by_name(cls, search_term):
        results = cls.objects.filter(name__icontains=search_term)
        return results

    def __str__(self):
        return self.name


class Comments(models.Model):
    image_commented_on = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image_comments')
    comment = models.CharField(max_length=255)
    comment_by = models.ForeignKey(User, related_name='uploaded_by', on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('comment_date',)
        verbose_name_plural = ('comments')


class Likes(models.Model):
    liked_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image_likes')
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('likes')

    def save_likes(self):
        self.save()

    def __str__(self):
        return f"{self.user.username}"


class Follow(models.Model):
    user_am_following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    user_following_me = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed_by')

    # @classmethod
    # def follow(cls,current_user,new):
    #     friends,created=cls.objects.get_or_create(current_user=current_user)
    #     friends.users.add(new)

    # @classmethod
    # def unfollow(cls,current_user,new):
    #     friends,created=cls.objects.get_or_create(current_user=current_user)
    #     friends.users.remove(new)
    
    @classmethod
    def get_followers(cls, follow_id):
        '''
        method to return a user's followers
        '''

        user = User.objects.filter(id = follow_id)

        followers = user.followers.all()
        return followers

    @classmethod
    def get_following(cls,follow_id):
        '''
        method to get all users that a user is following
        '''

        following = Follow.filter(follow = follow_id)

        return following
    
    def follow(self):
        self.save()

    def unfollow(self):
        self.delete()

    def __str__(self) -> str:
        return f"{self.user_following_me}"
