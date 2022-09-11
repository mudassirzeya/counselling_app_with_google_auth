from django.contrib import admin
from .models import UserProfile, StudentExtendedProfile, CounsellorExtendedProfile, Comment, Frequestly_Asked_Question
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(StudentExtendedProfile)
admin.site.register(CounsellorExtendedProfile)
admin.site.register(Comment)
admin.site.register(Frequestly_Asked_Question)
