from django.contrib import admin
from .models import Post, Category, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
    )
    list_editable = ('is_published',)
    search_fields = ('title', 'text',)
    list_filter = ('is_published', 'category', 'location',)
    list_per_page = 10

    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'author')
        }),
        ('Дополнительные параметры', {
            'fields': (
                'pub_date',
                'is_published',
                'category',
                'location'
            ),
            'description': 'Настройки публикации'
        })
    )

    help_texts = {
        'is_published': 'Снимите галочку, чтобы скрыть публикацию.',
        'pub_date': 'Если установить дату и время'
        'в будущем — можно делать отложенные публикации.'
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'is_published',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description',)
    list_filter = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}

    help_texts = {
        'is_published': 'Снимите галочку, чтобы скрыть категорию.',
        'slug': 'Идентификатор страницы для URL;'
        ' разрешены символы латиницы, цифры, дефис и подчёркивание.'
    }


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published',)
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)

    help_texts = {
        'is_published': 'Снимите галочку, чтобы скрыть местоположение.'
    }
