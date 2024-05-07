from django.shortcuts import render
from myapp.tasks import add
from celery.result import AsyncResult

# Create your views here.

def index(request):
    print("Results:")
    # result1 = add.delay(1,100)
    result1 = add.apply_async(args=[1,100])
    print(result1)
    return render(request, "myapp/home.html", {'result':result1})

def check_result(request, task_id):
     result = AsyncResult(task_id)
     return render(request, 'myapp/result.html',{'result':result})


def about(request):
    print("Results:")
    return render(request, "myapp/about.html")


def contact(request):
    print("Results:")
    return render(request, "myapp/contact.html")