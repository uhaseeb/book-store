from django.contrib import admin
from .models import Books, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", )
    list_filter = ('author', 'rating')


admin.site.register(Books, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
