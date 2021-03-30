from django.shortcuts import render


# Create your views here.
def hello_world(request):
    return render(request, "hello_world.html")


def fiver(request):
    context = {
        "message": "this is how we do",
    }
    return render(request, "fiver.html", context)
