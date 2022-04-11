from django.shortcuts import render


def home_view(request, *args, **kwargs):
    print(request)
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    print(request)
    return render(request, "about.html", {})
