from django.contrib import admin
from .models import bize_Ulasin

@admin.register(bize_Ulasin)
class BizeUlasin(admin.ModelAdmin):
    list_display = ["konu"]
    class Meta:
        model= bize_Ulasin
    

