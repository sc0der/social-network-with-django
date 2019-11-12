from django.shortcuts import render
from .models import Subject
from questions.models import Savolho

# Create your views here.
def by_subject(request, pk):
    savolho = Savolho.objects.filter(subject=pk)
    subjects = Subject.objects.all()
    current_subject = Subject.objects.get(pk=pk)
    context = {'savolho': savolho, 'subjects': subjects, 'current_subject': current_subject}
    return render (request,'questions/by_subject.html', context)