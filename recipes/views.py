from django.shortcuts import render


def home(request):
    return render(request,'recipes/pages/home.html')

"""ex de funções utilizadas como paginas dentro do aplicativo
def contato(request):
    return render(request, 'recipes/contato.html')

def sobre(request):
    return HttpResponse('Sobre1')"""
