from django.shortcuts import render

def base(request):
    return render(request, 'app2/base.html')
