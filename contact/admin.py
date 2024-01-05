from django.contrib import admin

from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "subject", "send_date"]
    list_display_links = ["first_name", "last_name", "email", "phone", "subject", "send_date"]