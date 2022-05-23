from django.shortcuts import render


def index(request):
    # if request.user.is_authentificated:
    #     return  # TODO redirect to calendar
    return render(request, 'index.html')


def calendar(request):
    return render(request, 'calendar.html')


def task(request):
    return render(request, 'task.html')