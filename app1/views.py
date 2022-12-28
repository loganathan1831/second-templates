from django.shortcuts import render

# Create your views here.
def file(request):
    return render(request,'file.html')