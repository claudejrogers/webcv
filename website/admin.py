from django.contrib import admin
from website.models import Author, Journal, Article, AuthorOrder, Carousel

admin.site.register(Author)
admin.site.register(Journal)
admin.site.register(Article)
admin.site.register(AuthorOrder)
admin.site.register(Carousel)
