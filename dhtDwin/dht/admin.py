# In admin.py
from django.contrib import admin
from .models import temphum, Status

admin.site.register(temphum)
admin.site.register(Status)
