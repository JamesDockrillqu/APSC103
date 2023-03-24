from django.contrib import admin

# Register your models here.

from .models import roadRatings, accountInfo

admin.site.register(roadRatings)
admin.site.register(accountInfo)
