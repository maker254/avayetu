from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from dbmaster.models import *

class NavSubMenuInline(admin.TabularInline):
      model=NavSubMenu

@admin.register(NavMainMenu)
class NavMenuAdmin(admin.ModelAdmin):
      inlines = [
        NavSubMenuInline, 
        ]