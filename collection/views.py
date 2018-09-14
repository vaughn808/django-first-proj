from django.shortcuts import render

# Create your views here.
def index(request):
    # My first views
    return render(request, 'index.html')
