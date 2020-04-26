from django.contrib import admin

# Register your models here.
from users.models import User, Code, TeacherInfo

admin.site.register(TeacherInfo)
admin.site.register(Code)
admin.site.register(User)
