from django.contrib import admin
from .models import Allergy

# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    search_fields = ['highLevelAllergy']

admin.site.register(Allergy,SearchAdmin)

