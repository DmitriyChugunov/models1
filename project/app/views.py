from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserForm, NewsForm, Product, DownloadForm, news_form
from .models import PostModel


def ProductView(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        country = request.POST.get("country")
        city = request.POST.get("city")
        street = request.POST.get("street")
        apartment = request.POST.get("apartment")
        number_house = request.POST.get("number_house")
        return HttpResponse(f'{name} {surname}, проверьте адрес доставки: <br>'
                            f'{country} <br>'
                            f'{city} <br>'
                            f'{street} <br>'
                            f'{number_house} <br>'
                            f'{apartment} <br>')
    else:
        form = Product()
    return render(request, 'dilivery.html', context={'form': form})


def shop(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f'User {name}, Age {age}')
    else:
        form = UserForm()
    return render(request, 'shop.html', context={'form': form})


def myForm(request):
    return render(request, 'form.html')


# def user(request):
#     name = request.POST.get("name")
#     age = request.POST.get("age")
#     return HttpResponse(f'User {name}, Age {age}')


def NewsView(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        is_publisher = request.POST.get("is_publisher")
        category = request.POST.get("category")
        return HttpResponse(f'Новость {title} <br>'
                            f'Контент: {content} <br>'
                            f'Категория {category}, {is_publisher}')
    else:
        form = NewsForm()
    return render(request, 'news.html', context={'form': form})


post = [
    {'id': 1, 'name': 'Открытие школы', 'text': 'В городе Елабуга была открыта новая общеобразовательная школа',
     'image': '/static/skoll.jpg'},
    {'id': 2, 'name': 'Новый завод Алабуги', 'text': 'В городе Елабуга был построен новый завод по производству студентов "Роботов"',
     'image': '/static/zavod.jpg'}
]


def PostsView(request):
    form = PostModel.objects.all()
    return render(request, 'postshtml.html', context={'form': form})


def DownloadView(request):
    form = DownloadForm()
    return render(request, 'Download.html', context={'form': form})


def create_view(request):
    if request.method == 'POST':
        form = news_form(request.POST)
        name = request.POST.get('name')
        text = request.POST.get('text')
        create = PostModel.objects.create(name=name, text=text)
        create.save()
        return redirect('all')
    form = news_form()
    return render(request, 'create.html', context={'form':form})


def delete_view(request, id):
    news = PostModel(pk=id)
    news.delete()
    return redirect('all')

def redact_view(request, id):
    news = PostModel.objects.get(pk=id)
    if request.method == 'POST':
        news = PostModel(pk=id)
        name = request.POST.get('name')
        text = request.POST.get('text')
        news.name = name
        news.text = text
        news.save()
        return redirect('all')
    form = news_form()
    return render(request, 'redact.html', context={'form':form})
