from django.contrib import admin
from app.models.user import User, Profile
from app.models.nomination import Symbol, Nomination

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Symbol)
admin.site.register(Nomination)
