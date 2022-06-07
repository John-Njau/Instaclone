from django.contrib import admin
from .models import Profile, Image, Comments, Follow

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comments)
# admin.site.register(Subscriber)
# admin.site.register(Likes)
admin.site.register(Follow)
