from django.shortcuts import render


# Страница "О нас"
def about(request):
    return render(request, 'pages/about.html')


# Страница "Правила"
def rules(request):
    return render(request, 'pages/rules.html')
