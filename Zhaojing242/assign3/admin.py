from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(File)
admin.site.register(Version)
admin.site.register(Comment)