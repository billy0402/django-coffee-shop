from django.contrib import admin

from .models import Coffee, OriginPlace, MainProcessing, Grinding

# Register your models here.
admin.site.register(Coffee)
admin.site.register(OriginPlace)
admin.site.register(MainProcessing)
admin.site.register(Grinding)
