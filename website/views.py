from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to DaveOttley.com. This is only the beginning.")
