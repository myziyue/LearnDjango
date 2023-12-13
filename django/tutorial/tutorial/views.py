from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse("<h1>You're at the index.</h1>")

def hello(request, username):
    print(username)
    return HttpResponse("<h1>You're at the index. Hello, " + username + "!</h1>")
