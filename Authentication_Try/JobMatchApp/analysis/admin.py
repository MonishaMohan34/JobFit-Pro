from django.contrib import admin

# Register your models here.
from .models import User

admin.site.register(User)


# analysis/admin.py
from .models import JobDescription

admin.site.register(JobDescription)
