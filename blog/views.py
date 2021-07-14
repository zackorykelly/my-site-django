from django.shortcuts import render

# Create your views here.


def posts_index(request):
    return render(request, "blog/index.html")


def posts_list(request):
    return render(request, "blog/list.html")


def posts_detail(request, slug):
    return render(request, "blog/detail.html")
