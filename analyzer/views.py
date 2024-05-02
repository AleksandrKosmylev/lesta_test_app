import os

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import ListView

from text_analyzer.settings import BASE_DIR, MEDIA_URL

from collections import defaultdict 

def index(request):
    # return HttpResponse("START")
    # return render(request, 'index.html', {'workers': Employees.objects.all()})
    context = {}
    text_analyze = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

        path = os.path.join(MEDIA_URL, uploaded_file.name)
        print(uploaded_file.name, 'name')

        d = defaultdict(int)
        with open(path, 'r') as my_file:
            # print(my_file.read())
            for line in my_file:
                # line.strip().split()
                for word in line.strip().split():
                    d[word] += 1
        print(d, 'dict')
        words_total = sum(d.values())
        print(sum(d.values()), 'words_total')
        for key, value in d.items():
            print(key, value, value/words_total)
    return render(request, 'upload.html', context)
