from django.contrib import admin
from app.models.user import User, Profile
from app.models.nomination import Symbol, Nomination
from app.models.vote import Vote

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Symbol)
admin.site.register(Nomination)
admin.site.register(Vote)
