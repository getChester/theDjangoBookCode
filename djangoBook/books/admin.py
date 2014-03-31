from django.contrib import admin
from books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)                             # tuple of fields to use to create filters along the right side
    date_hierarchy = 'publication_date'                             # date drill-down navigation bar at the top of the list
    ordering = ('-publication_date',)                               # ordered descending by their publication date
    fields = ('title', 'authors', 'publisher', 'publication_date')  # customizing edit forms
    filter_horizontal = ('authors', )

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)