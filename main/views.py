from django.shortcuts import render

def home_page(request):
    context = {}

    return render (request, 'main/index.html', context)
