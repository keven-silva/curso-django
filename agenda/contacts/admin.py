from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'phone',
                    'creation_date', 'category', 'show')
    list_display_links = ('id', 'name', 'last_name')
    # list_filter = ('name', 'last_name')
    list_per_oage = 10
    search_fields = ('id', 'name', 'last_name')

    list_editable = ('phone', 'show')

admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
