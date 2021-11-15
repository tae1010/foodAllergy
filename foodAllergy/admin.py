from django.contrib import admin
from .models import Allergy, Result

# Register your models here.

class SearchAdmin(admin.ModelAdmin):
    search_fields = ['highLevelAllergy']

admin.site.register(Allergy,SearchAdmin)
admin.site.register(Result)

