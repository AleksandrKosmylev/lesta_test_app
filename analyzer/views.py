import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from analyzer.models import Word
from text_analyzer.settings import MEDIA_URL
from collections import defaultdict


def index(request):
    context = {}
    if request.method == 'POST':

        # delete old data in table
        Word.objects.all().delete()

        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        path = os.path.join(MEDIA_URL, uploaded_file.name)
        d = defaultdict(int)
        with open(path, 'r', encoding='utf-8') as my_file:
            for line in my_file:
                for word in line.strip().split():
                    d[word] += 1
        words_total = sum(d.values())
        for key, value in d.items():
            Word.objects.create(name=key, tf=value, idf=value/words_total)

        # Delete uploaded file
        os.remove(path)

        model_data = Word.objects.values()[:50]
        context['model_data'] = model_data
    return render(request, 'upload.html', context)
