from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
    
def scikit(request):
    return render(request, 'base.html', {'poll': 'ff'})