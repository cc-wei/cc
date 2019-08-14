from django.Http import HttpResponse



def index(request):
    return HttpResponse("cc")


def login(request):
    return HttpResponse("dd")
