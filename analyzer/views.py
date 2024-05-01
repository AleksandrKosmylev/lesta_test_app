from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import ListView


def index(request):
    # return HttpResponse("START")
    # return render(request, 'index.html', {'workers': Employees.objects.all()})
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        print(uploaded_file.name)
    return render(request, 'upload.html', context)


"""
class IndexView(ListView):
    template_name = 'index.html'
"""