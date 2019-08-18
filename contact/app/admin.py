from django.contrib import admin

from .models import Contact

from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ContactAdmin(ImportExportModelAdmin):
    list_display = ('id','name', 'gender', 'email', 'info', 'phone')
    list_display_links = ('id', 'name')
    list_editable = ('info',)
    list_per_page = 8
    search_fields = ('name', 'gender', 'email', 'info', 'phone')
    list_filter = ('gender', 'date_added')

admin.site.register(Contact , ContactAdmin)
