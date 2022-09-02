from django.http import HttpResponse

def anunciar(request):
    return HttpResponse("Lista de Familiares")