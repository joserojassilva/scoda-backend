from django.contrib import admin
from .models import Pais, Region, Comuna

admin.site.register(Pais)
admin.site.register(Region)
admin.site.register(Comuna)