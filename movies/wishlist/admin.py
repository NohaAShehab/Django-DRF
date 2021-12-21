from django.contrib import admin
from wishlist.models import Movie, WishList, StreamPlatform, Reviews
# Register your models here.

admin.site.register(Movie)
admin.site.register(StreamPlatform)
admin.site.register(WishList)
admin.site.register(Reviews)


