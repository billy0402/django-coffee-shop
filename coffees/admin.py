from django.contrib import admin

from .models import Coffee, OriginPlace, Tag

# Register your models here.
admin.site.register(Coffee)
admin.site.register(OriginPlace)
admin.site.register(Tag)
