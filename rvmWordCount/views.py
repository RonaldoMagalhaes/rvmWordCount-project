from django.shortcuts import render
from collections import Counter


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split(" ")
    total_words = len(Counter(word_list))
    resume_words = Counter(word_list)

    return render(request, 'count.html', {'fulltext': fulltext, 'total': total_words, 'resume': resume_words})


def about(request):
    return render(request, 'about.html')
