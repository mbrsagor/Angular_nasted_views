from django.contrib import admin
from app.models.user import User, Profile

admin.site.register(User)
admin.site.register(Profile)
