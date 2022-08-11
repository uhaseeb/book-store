from django.contrib import admin
from .models import Books


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", )
    list_filter = ('author', 'rating')


admin.site.register(Books, BookAdmin)
