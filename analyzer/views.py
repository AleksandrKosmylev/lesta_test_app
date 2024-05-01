from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("START")
    # return render(request, 'index.html', {'workers': Employees.objects.all()})