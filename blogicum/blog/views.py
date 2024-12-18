from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category


# Главная страница
def index(request):
    current_time = timezone.now()
    posts = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=current_time  # Добавляем фильтр по дате публикации
    ).select_related('category', 'location', 'author')[:5]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


# View for the detail page
def post_detail(request, id):
    current_time = timezone.now()
    post = get_object_or_404(
        Post.objects.select_related('category'),
        id=id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=current_time  # Добавляем фильтр по дате публикации
    )
    return render(request, 'blog/detail.html', {'post': post})


# View for category page
def category_posts(request, category_slug):
    current_time = timezone.now()

    # Get category by slug or return 404
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)

    # Get all published posts for this category
    posts = Post.objects.filter(category=category,
                                is_published=True,
                                pub_date__lte=current_time,
                                category__is_published=True)

    context = {
        'category': category,
        'post_list': posts
    }
    return render(request, 'blog/category.html', context)
