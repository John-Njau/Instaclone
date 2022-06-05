from django.contrib import admin
from .models import Profile, Subscriber, Image, Comments

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comments)
admin.site.register(Subscriber)